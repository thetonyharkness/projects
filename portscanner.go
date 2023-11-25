package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

// Function to scan a specific port and perform banner grabbing
func scanPort(ip string, port int, wg *sync.WaitGroup) {
	defer wg.Done()

	address := fmt.Sprintf("%s:%d", ip, port)
	conn, err := net.Dial("tcp", address)
	if err != nil {
		return // Port is closed
	}
	defer conn.Close()

	// Set a timeout for reading from the connection
	conn.SetReadDeadline(time.Now().Add(2 * time.Second))

	// Read the banner from the connection
	banner, err := bufio.NewReader(conn).ReadString('\n')
	if err != nil {
		return // Unable to read banner
	}

	fmt.Printf("[+] Port %d is open on %s - %s\n", port, ip, strings.TrimSpace(banner))
}

func main() {
	fmt.Print("Enter the target host or CIDR range: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	target := scanner.Text()

	// Check if the target is a CIDR range
	ips, ipNet, err := net.ParseCIDR(target)
	if err != nil {
		// If not a CIDR range, use the target as is
		ip := net.ParseIP(target)
		if ip == nil {
			fmt.Println("Invalid target. Exiting.")
			return
		}
		target = ip.String()
	} else {
		// If CIDR range, use the network address and iterate over hosts
		target = ips.String()
	}

	fmt.Print("Enter the starting port: ")
	scanner.Scan()
	startPort, _ := strconv.Atoi(scanner.Text())

	fmt.Print("Enter the ending port: ")
	scanner.Scan()
	endPort, _ := strconv.Atoi(scanner.Text())

	// Use a WaitGroup to wait for all goroutines to finish
	var wg sync.WaitGroup

	// If the target is a CIDR range, iterate over hosts in the range
	if ipNet != nil {
		for ip := ips.Mask(ipNet.Mask); ipNet.Contains(ip); inc(ip) {
			for port := startPort; port <= endPort; port++ {
				// Increment the WaitGroup counter
				wg.Add(1)

				// Launch a goroutine for each port and IP combination
				go scanPort(ip.String(), port, &wg)
			}
		}
	} else {
		// If the target is a single host, iterate over ports
		for port := startPort; port <= endPort; port++ {
			// Increment the WaitGroup counter
			wg.Add(1)

			// Launch a goroutine for each port
			go scanPort(target, port, &wg)
		}
	}

	// Wait for all goroutines to finish
	wg.Wait()
}

// Function to increment an IP address
func inc(ip net.IP) {
	for j := len(ip) - 1; j >= 0; j-- {
		ip[j]++
		if ip[j] > 0 {
			break
		}
	}
}

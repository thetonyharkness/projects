# Enumerate Local Machine Information

# System Information
$systemInfo = Get-CimInstance -ClassName Win32_ComputerSystem
Write-Host "System Information"
Write-Host "------------------"
Write-Host "Manufacturer: $($systemInfo.Manufacturer)"
Write-Host "Model: $($systemInfo.Model)"
Write-Host "Operating System: $($systemInfo.Caption) $($systemInfo.Version)"
Write-Host "System Type: $($systemInfo.SystemType)"
Write-Host "Processor: $($systemInfo.SystemFamily) $($systemInfo.ProcessorType)"

# BIOS Information
$biosInfo = Get-CimInstance -ClassName Win32_BIOS
Write-Host "`nBIOS Information"
Write-Host "----------------"
Write-Host "BIOS Version: $($biosInfo.Version)"
Write-Host "Manufacturer: $($biosInfo.Manufacturer)"
Write-Host "Release Date: $($biosInfo.ReleaseDate)"
Write-Host "Serial Number: $($biosInfo.SerialNumber)"

# Processor Information
$processorInfo = Get-CimInstance -ClassName Win32_Processor
Write-Host "`nProcessor Information"
Write-Host "---------------------"
Write-Host "Processor: $($processorInfo.Name)"
Write-Host "Number of Cores: $($processorInfo.NumberOfCores)"
Write-Host "Number of Logical Processors: $($processorInfo.NumberOfLogicalProcessors)"
Write-Host "Architecture: $($processorInfo.Architecture)"

# Memory Information
$memoryInfo = Get-CimInstance -ClassName Win32_PhysicalMemory
$totalMemoryGB = [math]::Round(($memoryInfo | Measure-Object -Property Capacity -Sum).Sum / 1GB, 2)
Write-Host "`nMemory Information"
Write-Host "------------------"
Write-Host "Total Memory: ${totalMemoryGB}GB"
Write-Host "Memory Modules:"
foreach ($module in $memoryInfo) {
    Write-Host "  $($module.Capacity / 1GB)GB - $($module.Manufacturer) $($module.PartNumber)"
}

# Storage Information
$storageInfo = Get-CimInstance -ClassName Win32_DiskDrive
Write-Host "`nStorage Information"
Write-Host "-------------------"
foreach ($drive in $storageInfo) {
    Write-Host "Drive: $($drive.DeviceID)"
    Write-Host "  Model: $($drive.Model)"
    Write-Host "  Capacity: $($drive.Size / 1GB)GB"
}

# Network Adapter Information
$networkInfo = Get-CimInstance -ClassName Win32_NetworkAdapter | Where-Object { $_.PhysicalAdapter -eq $true }
Write-Host "`nNetwork Adapter Information"
Write-Host "------------------------"
foreach ($adapter in $networkInfo) {
    Write-Host "Adapter: $($adapter.Description)"
    Write-Host "  MAC Address: $($adapter.MACAddress)"
    Write-Host "  Speed: $($adapter.Speed) bps"
}

# Display Resolution Information
$displayInfo = Get-CimInstance -Namespace root/cimv2 -ClassName Win32_VideoController
Write-Host "`nDisplay Resolution Information"
Write-Host "---------------------------"
foreach ($display in $displayInfo) {
    Write-Host "Display Adapter: $($display.Name)"
    Write-Host "  Current Resolution: $($display.CurrentHorizontalResolution) x $($display.CurrentVerticalResolution)"
}

# Installed Software
$softwareInfo = Get-CimInstance -ClassName Win32_Product
Write-Host "`nInstalled Software"
Write-Host "------------------"
foreach ($software in $softwareInfo) {
    Write-Host "$($software.Name) $($software.Version)"
}

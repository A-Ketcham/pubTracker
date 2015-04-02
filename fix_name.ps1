#
#See: http://blogs.technet.com/b/heyscriptingguy/archive/2008/01/17/how-can-i-use-windows-powershell-to-replace-characters-in-a-text-file.aspx
 
param([string]$name = $(throw "Use the -name parameter to specify your project's name."))
Get-ChildItem . -File | ForEach {
  (Get-Content $_ )| ForEach {$_ -replace "\{\{ project_name \}\}", $name} | Set-Content $_ 
}

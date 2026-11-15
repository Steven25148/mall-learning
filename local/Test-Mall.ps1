$ErrorActionPreference='Stop'
$guestIp=((wsl -d Ubuntu-24.04 -- hostname -I).Trim() -split '\s+')[0]
$login=Invoke-RestMethod "http://${guestIp}:8080/admin/login" -Method Post -ContentType application/json -Body '{"username":"admin","password":"macro123"}'
if($login.code -ne 200){throw 'Login failed'}
$headers=@{Authorization=$login.data.tokenHead+$login.data.token}
$products=Invoke-RestMethod "http://${guestIp}:8080/product/list?pageNum=1&pageSize=5" -Headers $headers
$portalHome=Invoke-RestMethod "http://${guestIp}:8085/home/content"
$search=Invoke-RestMethod "http://${guestIp}:8081/esProduct/search/simple?keyword=%E5%B0%8F%E7%B1%B3"
if($products.code -ne 200 -or $portalHome.code -ne 200 -or $search.code -ne 200 -or $search.data.total -lt 1){throw 'API smoke check failed'}
[pscustomobject]@{checkedAt=(Get-Date -Format o);login=$login.code;products=$products.code;productCount=$products.data.total;home=$portalHome.code;search=$search.code;searchMatches=$search.data.total} | ConvertTo-Json | Tee-Object -FilePath "$PSScriptRoot\verification.json"

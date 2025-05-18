param($action)

function Convert-UrlsToClean {
    Write-Host "Converting URLs to clean format..."
    Get-ChildItem -Path . -Recurse -File -Filter "*.html" | ForEach-Object {
        if ($_.FullName -notmatch "\\.git\\") {
            try {
                $content = Get-Content $_.FullName -Raw
                $newContent = $content -replace "\\.html", "/"
                Set-Content -Path $_.FullName -Value $newContent -Encoding UTF8
            }
            catch {
                Write-Host "Error processing $($_.FullName): $_"
            }
        }
    }
}

function Convert-UrlsToHtml {
    Write-Host "Converting URLs to .html format for development..."
    Get-ChildItem -Path . -Recurse -File -Filter "*.html" | ForEach-Object {
        if ($_.FullName -notmatch "\\.git\\") {
            try {
                $content = Get-Content $_.FullName -Raw
                $newContent = $content -replace "/index/", "/index.html"
                $newContent = $newContent -replace "/products/([^/]+)/", "/products/$1.html"
                Set-Content -Path $_.FullName -Value $newContent -Encoding UTF8
            }
            catch {
                Write-Host "Error processing $($_.FullName): $_"
            }
        }
    }
}

# Виконати конвертацію відповідно до переданого параметра
if ($action -eq "clean") {
    Convert-UrlsToClean
}
elseif ($action -eq "html") {
    Convert-UrlsToHtml
}

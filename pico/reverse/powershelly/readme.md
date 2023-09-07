# Powershelly

## Anaylze
- Check `input.txt`
  - **Wrong format 5**
    - `Get-Content` v.s. `ReadAllbytes`
      ```powershell
      $out = Get-Content -Path $input
      $enc = [System.IO.File]::ReadAllBytes("$input")
      ```
      - `if ($out.Length -gt 5 -or $enc.count -ne $numLength)`
        Indicate that, in order to pass the check, the two methods of reading file can result in different in length. However, I have no idea how it can be achieved. From [Microsoft document's](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content?view=powershell-7.1) example (as the example below), 
        ```powershell
        $raw = Get-Content -Path .\LineNumbers.txt -Raw
        $lines = Get-Content -Path .\LineNumbers.txt
        Write-Host "Raw contains $($raw.Count) lines."
        Write-Host "Lines contains $($lines.Count) lines."

        Raw contains 1 lines.
        Lines contains 100 lines.
        ```
        without parameter `-Raw`, `Get-Content` returns as an array of newline-delimited strings and `Length` will be the number of lines when the file contains more than one line.  
        Therefore, to pass the check, `input.txt` contains between **2 to 5 lines** and has `$numLength` characters.
  - **Wrong format 1/0/**
    - `if (($enc[$i] -ne 49) -and ($enc[$i] -ne 48) -and ($enc[$i] -ne 10) -and ($enc[$i] -ne 13) -and ($enc[$i] -ne 32))`
      - contain only `1`, `0`, `\n`, `\r`, ` ` five different characters
  - **Wrong Format 6**
    For every line, all words seperated by `space` contain only *6 characters*.
- modification on `input.txt`

## Input.txt to flag


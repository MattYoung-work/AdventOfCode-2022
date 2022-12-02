$foo = Get-Content ./input.txt
$max = 0
$max_pos = 0
$curr = 0
$curr_pos = 0

$foo | %{
    if($_ -eq ""){
        Write-Output "Elf $curr_pos has $curr"
        if($curr -gt $max){
            $max = $curr
            $max_pos = $curr_pos
            }
        $curr = 0
        $curr_pos += 1
        }
    else{
        $curr = $curr + $_
        }
    }
$max
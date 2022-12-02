$foo = Get-Content ./input.txt
$curr = 0
$elves = @()


$foo | %{
    if($_ -eq ""){
        $elves += $curr
        $curr = 0
        }
    else{
        $curr = $curr + $_
        }
    }
$elves = $elves | Sort -Descending
$elves[0]+$elves[1]+$elves[2]
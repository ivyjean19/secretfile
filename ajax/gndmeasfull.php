

<?php   
    if(isset($_GET['gsite'])) {
        $gsite = $_GET['gsite'];
    }
    else {
        echo "Error: No value for site has been set";
        return -1;
    }
  


    $os = PHP_OS;
    //echo "Operating System: $os <Br>";

    if (strpos($os,'WIN') !== false) {
        $pythonPath = 'c:\Users\USER\Anaconda2\python.exe';
    }
    elseif ((strpos($os,'Ubuntu') !== false) || (strpos($os,'Linux') !== false)) {
<<<<<<< HEAD
        $pythonPath = '/home/dews/anaconda/bin/python';
        // echo "hoy nsa dews ako";
=======
        $pythonPath = '/home/ubuntu/anaconda2/bin/python';
        // echo "hoy nsa ubuntu ako";
>>>>>>> 689de32cd89f5608111837387342245cca39a362
    }
    else {
        echo "Unknown OS for execution... Script discontinued";
        return;
    }

    //For Linux (Remember to set one for windows as well)
    
    $fileName = 'gndmeasfull.py';
    $command = $pythonPath.' '.$fileName.' '.$gsite;

    // echo "$command";
    exec($command, $output, $return);
    echo($output[0]);

    
?>
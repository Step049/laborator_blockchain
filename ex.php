<?php
echo   "\n\n";
// echo PHP_INT_MIN . "\n\n";
//     function factorial($n) 
// {
//  if ($n <= 1) return 1; 
//  return $n * factorial($n - 1); // здесь происходит повторный вызов функции 
// } 

// $s = factorial(21);

// if ($s > PHP_INT_MIN){
//     echo "YYY \n\n";
// }
// else{
//     echo "NNN \n\n";
// }
// echo var_dump($s);

// $arr = [1,2,[], new TypeError("")];
// foreach ($arr as $val):
//     echo var_dump($val);
//     endforeach;

class BoolError extends Exception{
    function __construct($message){

        parent:: __construct($message);

    }

    public function getMessageError() {
        return parent::getMessage() . "Bool " . "\n";
    }

}

class StringError extends Exception{
    function __construct($message){

        parent:: __construct($message);

    }

    public function getMessageError() {
        return parent::getMessage() . "String " . "\n";
    }
}

class IntegerError extends Exception{
    function __construct($message){

        parent:: __construct($message);

    }

    public function getMessageError() {
        return parent::getMessage() . "Integer " . "\n";
    }
}
class DoubleError extends Exception{
    function __construct($message){

        parent:: __construct($message);

    }

    public function getMessageError() {
        return parent::getMessage() . "Double " . "\n";
    }
}

class NullError extends Exception{
    function __construct($message){

        parent:: __construct($message);

    }

    public function getMessageError() {
        return parent::getMessage() . "Null " . "\n";
    }
}

class ArrayError extends Exception{
    function __construct($message){

        parent:: __construct($message);

    }

    public function getMessageError() {
        return parent::getMessage() . "Array " . "\n";
    }
}

class ObjectError extends Exception{
    function __construct($message){

        parent:: __construct($message);

    }

    public function getMessageError() {
        return parent::getMessage() . "Object " . "\n";
    }
}


$arrClass = [

    "boolean" => "BoolError",
    "string" => "StringError",
    "integer" => "IntegerError",
    "double" => "DoubleError",
    "NULL" => "NullError",
    "array" => "ArrayError",
    "object" => "ObjectError"

];

// $var = '';

// $clas = $arrClass[gettype($var)];

// $ves = new $clas("Вы ввели неподходящий тип данных для данной программы: ");

// echo $ves->getMessageError();












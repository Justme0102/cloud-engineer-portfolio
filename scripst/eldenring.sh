#!/bin/bash

echo "select your clash if you wanna continua 1- samuro 2-pariguayo 3-el medio gay"

read class

case  $class in 
      1)    type="samuro"
            hp=20
            power=15
            ;;

      2)    type="pariguayo"
            hp=14
            power=45
            ;;
  
      3)    type="el medio gay"
            hp=18
            power=3
            ;;
esac 

echo "$type this is your hp $hp and this is your power $power"

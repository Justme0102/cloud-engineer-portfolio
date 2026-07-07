#!/bin/bash

echo "what is your name" 

read name 

echo "how old are you"

read age 


echo "hello $name your age is $age"

getrich=$((( $RANDOM % 15 ) + $age ))

echo "hello $name you gonna be a bilioner when you are $getrich years old"



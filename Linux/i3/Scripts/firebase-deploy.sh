#!/bin/bash

read -p "Build? y/n " -n 1 -r build

if [[ $build == "y" ]];
    then yarn build;
else
    echo "No build"
fi

echo 

read -p "Deploy to Firebase? y/n " -n 1 -r firebase

if [[ $firebase == "y" ]];
    then firebase deploy;
else
    echo "Bye"
fi


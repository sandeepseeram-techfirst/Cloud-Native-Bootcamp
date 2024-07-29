# Introduction 
new and efficient programming language for data science called Julia.

docker run -it --rm julia:1.9.3-bullseye 

$ using Statistics
$ function descriptive_statistics(x)
    m = mean(x)
    sd = std(x)
    return Dict("mean" => m, "std_dev" => sd)
  end


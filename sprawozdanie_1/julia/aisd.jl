function func(y, z)
    return 108 - (815 - 1500 / y) / z
end

function prec_16()
    x = Float16[4, 4.25]
    i = 1
    tmp = 0
    lista = []

    while tmp < 6
        tmp = func(x[i], x[i+1])
        push!(x, tmp)                           #push! = append
        println(i,' ', tmp)
        i += 1
        
        push!(lista, abs(tmp - 5))
    end
    print(findmin(lista))
end

function prec_32()
    x = Float32[4, 4.25]
    i = 1
    tmp = 0
    lista = []

    while tmp < 6
        tmp = func(x[i], x[i+1])
        push!(x, tmp)
        println(i,' ', tmp)
        i += 1
        
        push!(lista, abs(tmp - 5))
    end
    print(findmin(lista))
end
function prec_64()
    x = Float64[4, 4.25]
    i = 1
    tmp = 0
    lista = []

    while tmp < 6
        tmp = func(x[i], x[i+1])
        push!(x, tmp)
        println(i,' ', tmp)
        i += 1
        
        push!(lista, abs(tmp - 5))
    end
    print(findmin(lista))
end

function prec_128()
    setprecision(128)
    x = BigFloat[4, 4.25]
    i = 1
    tmp = 0
    lista = []

    while tmp < 6
        tmp = func(x[i], x[i+1])
        push!(x, tmp)
        println(i,' ', tmp)
        i += 1
        
        push!(lista, abs(tmp - 5))
    end
    print(findmin(lista))
end

function prec_256()
    setprecision(256)
    x = BigFloat[4, 4.25]
    i = 1
    tmp = 0
    lista = []

    while tmp < 6
        tmp = func(x[i], x[i+1])
        push!(x, tmp)
        println(i,' ', tmp)
        i += 1
        
        push!(lista, abs(tmp - 5))
    end
    print(findmin(lista))
end

prec_16()       #1
prec_32()      #5
#prec_64()      #10
#prec_128()      #25
#prec_256()     #50



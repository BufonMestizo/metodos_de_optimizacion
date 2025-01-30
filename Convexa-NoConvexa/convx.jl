using Plots
#funcion
f(x) = x^2  # f(x) = x^2 es convexa

x_min, x_max = -2, 2  # Intervalo de evaluación
x_vals = range(x_min, x_max, length=100)  # Puntos para graficar

plot(x_vals, f.(x_vals), label="f(x)", linewidth=2, legend=:topleft)

x1, x2 = -1.5, 1.5
λ = 0.5

x_mid = λ * x1 + (1 - λ) * x2
f_mid = f(x_mid)

convex_comb = λ * f(x1) + (1 - λ) * f(x2)

println("f($x_mid) = $f_mid")
println("Convex Combination: $convex_comb")
if f_mid <= convex_comb
    println("✅ La función es convexa en el dominio.")
else
    println("❌ La función no es convexa en el dominio.")
end

scatter!([x1, x2], [f(x1), f(x2)], label="Puntos (x1, x2)", markersize=5)
plot!([x1, x2], [f(x1), f(x2)], linestyle=:dash, label="Cuerda", linewidth=2)

scatter!([x_mid], [f_mid], label="Punto Intermedio", markersize=5, color=:red)

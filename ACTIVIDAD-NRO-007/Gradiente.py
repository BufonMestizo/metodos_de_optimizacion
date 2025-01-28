import numpy as np

# Ejercicio 1: Mínimo de una función cuadrática en 1D
def ejercicio1():
    def g(x):
        return (x - 5) ** 2

    def grad_g(x):
        return 2 * (x - 5)

    x0 = 10
    eta = 0.2
    iterations = 5
    x = x0
    results = []

    for k in range(iterations + 1):
        gx = g(x)
        results.append((k, x, gx))
        if k < iterations:
            x = x - eta * grad_g(x)

    print("Ejercicio 1: Mínimo de una función cuadrática en 1D")
    print("Iteración | x_k | g(x_k)")
    for result in results:
        print(f"{result[0]:9} | {result[1]:.4f} | {result[2]:.4f}")

# Ejercicio 2: Ajuste de una recta con descenso del gradiente
def ejercicio2():
    # Datos
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 2.8, 3.6, 4.5, 5.1])

    def J(beta0, beta1):
        return np.sum((y - (beta0 + beta1 * X)) ** 2)

    def grad_J(beta0, beta1):
        grad_beta0 = -2 * np.sum(y - (beta0 + beta1 * X))
        grad_beta1 = -2 * np.sum((y - (beta0 + beta1 * X)) * X)
        return grad_beta0, grad_beta1

    beta0, beta1 = 0, 0
    eta = 0.01
    iterations = 3
    results = []

    for k in range(iterations + 1):
        cost = J(beta0, beta1)
        results.append((k, beta0, beta1, cost))
        if k < iterations:
            grad0, grad1 = grad_J(beta0, beta1)
            beta0 = beta0 - eta * grad0
            beta1 = beta1 - eta * grad1

    print("\nEjercicio 2: Ajuste de una recta con descenso del gradiente")
    print("Iteración | beta0 | beta1 | Costo J")
    for result in results:
        print(f"{result[0]:9} | {result[1]:.4f} | {result[2]:.4f} | {result[3]:.4f}")

# Ejercicio 3: Clasificación logística con descenso del gradiente
def ejercicio3():
    # Datos
    X = np.array([[0.5, 1.0], [1.5, 2.0], [2.0, 2.5], [3.0, 3.5]])
    y = np.array([0, 0, 1, 1])

    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    def logistic_cost(w):
        z = np.dot(X, w[1:]) + w[0]
        predictions = sigmoid(z)
        return -np.mean(y * np.log(predictions) + (1 - y) * np.log(1 - predictions))

    def grad_logistic_cost(w):
        z = np.dot(X, w[1:]) + w[0]
        predictions = sigmoid(z)
        error = predictions - y
        grad_w0 = np.mean(error)
        grad_w1 = np.mean(error[:, np.newaxis] * X, axis=0)
        return np.concatenate(([grad_w0], grad_w1))

    w = np.array([0.0, 0.0, 0.0])
    eta = 0.1
    iterations = 3
    results = []

    for k in range(iterations + 1):
        cost = logistic_cost(w)
        results.append((k, w.copy(), cost))
        if k < iterations:
            grad = grad_logistic_cost(w)
            w = w - eta * grad

    print("\nEjercicio 3: Clasificación logística con descenso del gradiente")
    print("Iteración | Pesos w | Costo J")
    for result in results:
        print(f"{result[0]:9} | {result[1]} | {result[2]:.4f}")

# Ejercicio 4: Descenso del gradiente estocástico (SGD)
def ejercicio4():
    # Datos hipotéticos
    np.random.seed(42)
    N = 1000
    X = np.random.randn(N, 3)
    y = np.random.randn(N)

    def J(w):
        return np.mean((y - np.dot(X, w)) ** 2)

    def grad_J_minibatch(w, minibatch):
        X_batch, y_batch = minibatch
        predictions = np.dot(X_batch, w)
        error = predictions - y_batch
        return -2 * np.mean(error[:, np.newaxis] * X_batch, axis=0)

    w = np.zeros(3)
    eta = 0.01
    batch_size = 50
    iterations = 3
    results = []

    for k in range(iterations + 1):
        cost = J(w)
        results.append((k, w.copy(), cost))
        if k < iterations:
            indices = np.random.choice(N, batch_size, replace=False)
            minibatch = (X[indices], y[indices])
            grad = grad_J_minibatch(w, minibatch)
            w = w - eta * grad

    print("\nEjercicio 4: Descenso del gradiente estocástico (SGD)")
    print("Iteración | Pesos w | Costo J")
    for result in results:
        print(f"{result[0]:9} | {result[1]} | {result[2]:.4f}")

# Ejecutar todos los ejercicios
ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()

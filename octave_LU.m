A = [1 4 9 16;
     4 9 16 25;
     9 16 25 36;
     16 25 36 49];

b = [30; 54; 86; 126];

n = size(A, 1);
L = eye(n);
U = A;

for i = 1:n
    for j = i+1:n
        factor = U(j, i) / U(i, i);
        L(j, i) = factor;
        U(j, i:end) = U(j, i:end) - factor * U(i, i:end);
    end
end

y = zeros(n, 1);
for i = 1:n
    y(i) = b(i) - L(i, 1:i-1) * y(1:i-1);
end

x = zeros(n, 1);
for i = n:-1:1
    x(i) = (y(i) - U(i, i+1:end) * x(i+1:end)) / U(i, i);
end


disp("Resultado = "), disp(x)


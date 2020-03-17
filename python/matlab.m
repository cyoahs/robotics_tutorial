
a = 0:11;
a = reshape(a, [3, 4]);
b = 0:7;
b = reshape(b, [4, 2]);
% martix multiplication
c = a*b;
% element-wise multiplication
d = a.*a;
% bool index
d(d > 6) = 0;
% sin
sin(a);
% shape
size(a);
% concatenate
[a, b]
[a; b]


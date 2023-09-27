pkg load statistics

# a)
alfa = input('alfa = ', 's'); # 0.5
beta = input('beta = ', 's'); # 0.5

option = input('distr = ', 's');
switch option
  case 'normal'
    fprintf('a)\n');
    miu = input('miu = ');
    sigma = input('sigma = ');
    p1 = normcdf(0,miu, sigma);
    fprintf('P(X<=0)=%1.3f\n', p1);
    p2 = 1 - p1;
    fprintf('P(X>=0)=%1.3f\n', p2);
    fprintf('b)\n');
    p3 = normcdf(1, miu, sigma) - normcdf(-1, miu, sigma);
    p4 = 1 - p3;
    fprintf('P(-1<=X<=1)=%1.4f\n', p3);
    fprintf('P(X<=-1 or X>=1)=%1.4f\n', p4);
    fprintf('c)\n');
    p5 = norminv(alfa, miu, sigma);
    p6 = norminv(1 - beta, miu, sigma);
    fprintf('%1.4f\n', p5);
    fprintf('d)\n');
    fprintf('%1.4f\n', p6);


  case 'student'
    fprintf('a)\n');
    n = input('n = ');
    p1 = tcdf(0, n);
    fprintf('P(X<=0)=%1.3f\n', p3);
    p2 = 1 - p1;
    fprintf('P(X>=0)=%1.3f\n', p4);
    fprintf('b)\n');
    p3 = tcdf(1, n) - tcdf(-1, n);
    p4 = 1 - p3;
    fprintf('P(-1<=X<=1)=%1.4f\n', p3);
    fprintf('P(X<=-1 or X>=1)=%1.4f\n', p4);
    fprintf('c)\n');
    p5 = tinv(alfa, n);
    p6 = tinv(1 - beta, n);
    fprintf('%1.4f\n', p5);
    fprintf('d)\n');
    fprintf('%1.4f\n', p6);

  case 'fischer'
    fprintf('a)\n');
    m = input('m = ');
    n = input('n = ');
    p1 = fcdf(0, m, n);
    fprintf('P(X<=0)=%1.3f\n', p5);
    p2 = 1 - p1;
    fprintf('P(X>=0)=%1.3f\n', p6);
    fprintf('b)\n');
    p3 = fcdf(1, m, n) - fcdf(-1, m, n);
    p4 = 1 - p3;
    fprintf('P(-1<=X<=1)=%1.4f\n', p3);
    fprintf('P(X<=-1 or X>=1)=%1.4f\n', p4);
    fprintf('c)\n');
    p5 = finv(alfa, m, n);
    p6 = finv(1 - beta, m, n);
    fprintf('%1.4f\n', p5);
    fprintf('d)\n');
    fprintf('%1.4f\n', p6);

  otherwise
    fprintf('Error\n');
  end

  p = input('p = ')
    for n=1:3:100
      k = 0:n
      prob = binopdf(k,n,p)
      plot(prob)
      pause(0.2)
    endfor

  n = input('n = ')
  p = input('p = ')
  lambda = n * p
  k = 0:n
  p1 = poisspdf(k, lambda)
  p2 = binopdf(k,n,p)
  plot(k,p1,k,p2)


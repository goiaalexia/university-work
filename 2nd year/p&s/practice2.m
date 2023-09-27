%Ex2-drive
%5 To reach the maximum efficiency in performing an assembling operation in a manufacturing plant, new employees are required to take a 1-month training course. A new method was suggested, and the manaager wants to compare the new method with the standard one,by looking at the lengths of time required for employees to assemble a certain device. they are given below (and assumed approximately normally distributed):
%Assembling times:(Standard 46,37,39,48,47,44,35,32,44,37)(New:34,33,31,35,34,30,27,32,31,31)
%a) At the 5% significance level, do the population variances seem to differ?
%b)Find a 95% confidence interval for the difference of the average assembling times.


standard = [46,37,39,48,47,44,35,32,44,37];
new = [34,33,31,35,34,30,27,32,31,31];
alpha = 0.05;

%a)
fprintf('\n Part a. Comparing variances\n')
[h,p,ci,stats]=vartest2(standard ,new, 'alpha',alpha,'tail','left')
if h == 0
    fprintf("The variances are not significantly different at the %g level.\n",alpha);
else
    fprintf("The variances are significantly different at the %g level.\n",alpha);
end

%b)
fprintf('\n Part b3. The Welch s t-test when variances are not assumed to be equal.\n')
x = [46,37,39,48,47,44,35,32,44,37];
y = [34,33,31,35,34,30,27,32,31,31];
alpha = 0.05;
critical_value = tinv(1-alpha/2, length(x)-1);
[h,p,ci,stats] = ttest2(x, y, 'alpha',alpha,'tail','left')

fprintf('95%% Confidence interval for the difference of the average assembling time is [%.3f, %.3f]\n', ci(1), ci(2));

 % b
    v_standard = var(x_standard);
    v_new = var(x_new); %variance

    % The null hypothesis H0: mu1 = mu2
    % The alt. hypothesis H1: mu1 > mu2
    % right-tailed for the difference of means

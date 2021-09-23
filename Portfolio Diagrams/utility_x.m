a=0;b=1;W=10;x = 0:10/100:50;
y = b*log(x/W + 1) + a;
plot(x,y,'Color','k','LineWidth',1.5)
axes = [0 inf];
ylim(axes)
xlim(axes)
xticks([0])
xticklabels({0})
yticks([0])
yticklabels({0})
title('Utility Function (Logarithmic)')
xlabel('Wealth, $x$','Interpreter','latex')
ylabel('$U(x)$','Interpreter','latex')
saveas(gcf,'utility_log','png')
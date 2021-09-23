a=0;b=1;W=10;x = 0:10/100:50;
y = b*log(x/W + 1) + a;
figure(1)
set(groot,'defaultAxesTickLabelInterpreter','latex');  
plot(x,y,'Color','k','LineWidth',1)
axes = [0 inf];
ylim(axes)
xlim(axes)
title('Utility Function (Logarithmic)')
xlabel('Wealth, $x$','Interpreter','latex')
ylabel('$U(x)$','Interpreter','latex')
hold on

%points 1 and 2
x1=7;
x2=40;
y1=b*log(x1/W + 1)+a;
y2=b*log(x2/W + 1)+a;

%midpoint
xm = 0.5*(x1 + x2);
ym = 0.5*(y1 + y2);

%plot points
plot([x1 x2], [y1 y2], '-','Color',[0.1 0.7 0],'LineWidth',1.1)
plot(xm,ym,'.k','MarkerSize',20)
text(x1+0.3,y1-0.05,'P1')
text(x2+0.3,y2-0.05,'P2')
plot(x1,y1,'.k','MarkerSize',20)
plot(x2,y2,'.k','MarkerSize',20)

%plot index to curve values
plot([xm xm], [0 b*log(xm/W + 1)],':k')
plot([0 xm], [b*log(xm/W + 1) b*log(xm/W + 1)],':k')
d=5;
plot([xm-d xm-d], [0 b*log((xm-d)/W + 1)],':k')
plot([0 xm-d], [b*log((xm-d)/W + 1) b*log((xm-d)/W + 1)],':k')
plot(xm-d,b*log((xm-d)/W + 1),'.k','MarkerSize',15)
plot(xm,b*log(xm/W + 1),'.k','MarkerSize',15)
plot([x1 x1], [0 b*log(x1/W + 1)],':k')
plot([0 x1], [b*log(x1/W + 1) b*log(x1/W + 1)],':k')
plot([x2 x2], [0 b*log(x2/W + 1)],':k')
plot([0 x2], [b*log(x2/W + 1) b*log(x2/W + 1)],':k')


xticks([0, x1, xm-d, xm, x2])
xticklabels({'0', '$x_1$', '$\bar{y}$' ,'$\bar{x}$', '$x_2$'})
yticks([0, b*log(x1/W + 1), b*log((xm-d)/W + 1), b*log(xm/W + 1), b*log(x2/W + 1)])
yticklabels({'0', '$u_1$', '$\bar{u}$','$\bar{v}$', '$u_2$'})

saveas(gcf,'riska','png')
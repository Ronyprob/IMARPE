# Datos pegados de la ejecución en Python

#C<-c( 2, 5, 18 , 29, 32)
#N<-c( 357,  669.874 ,  716.7670 , 667.863 , 694.053 )
#plot(x=C, y=N, type = 'l', xlab = 'cantidad capturada', ylab = 'población total')



# Datos extraidos de la ejecución en Python
x <- as.numeric(data[1:1,2:6])
y <- as.numeric(data[2:2,2:6])
plot(x,y, type="l")

class pizza():
  service_tax = 30
  __gst=20 # hidden to particular class only


  def __init__(self,name,size,base,topping):
    self.size=size
    self.name=name
    self.base=base
    self.topping=topping


  def print_gst(self):
    print("gst value is",self.__gst)

  def generate_bill(self):
    menu={"margerita":300,"Mexican Chilli":400,"Peppy Paneer":450}
    for i,j in menu.items():
      if(self.name==i):
        print("Bill is",j+self.service_tax+self.__gst)

pizza1=pizza("Peppy Paneer","R","cheese burst","green olives")# defining instance
pizza1.generate_bill()# accessing method
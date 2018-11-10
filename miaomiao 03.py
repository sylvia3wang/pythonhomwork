class RentalUnit:
 def get_name(self):
   full_name = self.tenant_first + " " + self.tenant_last
   return full_name


unit1 = RentalUnit()
unit1.address = "155 East 55th Street"
unit1.rent = 5000
unit1.tenant_first = "John"
unit1.tenant_last = "Smith"
unit1.eviction = False

print(unit1.get_name())

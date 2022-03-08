class Weapon:
    def __init__(self, kind, length, weight, material, durability: int):
        self.kind = kind
        self.length = length
        self.weight = weight
        self.material = material
        self.durability = durability

    def hold_weapon(self):
        out = f"You have held the weapon. It weights {self.weight}"
        return out

    def get_kind(self):
        out = f"This weapon is {self.kind}"
        return out

    def use_weapon(self):
        self.durability -= 5
        out = f"You have used your weapon, the durability is now {self.durability}"
        return out

    def repair_weapon(self):
        self.durability += 20
        out = f"The weapon is repaired, and durability is now {self.durability}"
        return out

    def reforge(self, custom):
        self.material = custom
        out = f"Your weapon has been reforged."
        return out

    def __repr__(self):
        out = f"-Your weapon-\n " \
              f"Kind: {self.kind}\n " \
              f"Length: {self.length}\n " \
              f"Weight: {self.weight}\n " \
              f"Material: {self.material}\n " \
              f"Durability: {self.durability}"
        return out


class Gun(Weapon):
    def __init__(self, name, magazine_capacity: int, company, sub_attachment: list, price: int,
                 kind, length, weight, material, durability: int):
        super().__init__(kind, length, weight, material, durability)
        self.magazine = magazine_capacity
        self.name = name
        self.company = company
        self.sub_attachment = sub_attachment
        self.price = price
        self.ammo = Ammo(size=20, diameter=20, gun_type="Machine Gun", quantity=30, country="USA")

    def __repr__(self):
        out = f"-Your Gun-\n " \
              f"Name: {self.name}\n " \
              f"Magazine: {self.magazine}\n " \
              f"Company: {self.company}\n " \
              f"Attachments: {self.sub_attachment}\n " \
              f"Price: {self.price}$"
        return out

    def shoot(self, new: int):
        self.magazine -= new
        out = f"You shot {new} bullets.\n" \
              f"Ammo left: {self.magazine}"
        return out

    def add_attachment(self, new):
        self.sub_attachment.append(new)
        out = f"Now your gun has attachments listed below\n" \
              f"{self.sub_attachment}"

    def get_ammo_left(self):
        out = f"You have {self.magazine} bullets left in your magazine."
        return out

    def sell(self):
        out = f"You have sold your gun at the price of {self.price}$"
        return out

    def reload(self):
        self.magazine += self.ammo.quantity
        out = f"Ammo reloaded"
        return out


class Ammo:
    def __init__(self, size: int, diameter: int, gun_type, quantity: int, country):
        self.size = size
        self.diameter = diameter
        self.gun_type = gun_type
        self.quantity = quantity
        self.country = country

    def __repr__(self):
        out = f"-Your Ammo-\n " \
              f"Size: {self.size}\n " \
              f"Diameter: {self.diameter}\n " \
              f"Type of Gun: {self.gun_type}\n " \
              f"Quantity: {self.quantity}\n " \
              f"Country: {self.country}"
        return out

    def throw_ammo(self):
        out = "You threw your ammo away."
        self.quantity = 0
        return out

    def get_gun_type(self):
        out = f"The gun type this ammo can be used for is {self.gun_type}"
        return out

    def get_ammo(self, new):
        self.quantity += new
        out = f"You earned {new} extra bullets"
        return out

    def ammo_quantity(self):
        out = f"Ammo Quantity: {self.quantity}"
        return out

    def get_country(self):
        out = f"This ammo is from {self.country}"
        return out


正宗 = Weapon("Katana", "97cm", "2kg", "Steel", 100)
Gungnir = Weapon("Lance", "70cm", "4kg", "Metal", 150)
Gun1 = Gun("Desert Eagle", 9, "Pearl River", ["Silencer", "Laser Pointer"], 2000, "Pistol", "26cm", "1kg", "steel", 100)
Gun2 = Gun("AK-47", 30, "Izhmash", ["6x Scope", "Long Barrel"], 800, "Assault Rifle", "80cm", "3.8kg", "Steel", 200)
Ammo1 = Ammo(10,10,"Pistol",6,"Russia")


# Tests for Class Weapon
print(Gungnir.reforge())
print(Gungnir)
print(正宗.use_weapon())
print(正宗.repair_weapon())


# Tests for Class Gun
print(Gun2)
print(Gun2.shoot(30))
print(Gun2.reload())
print(Gun2.get_ammo_left())


# Tests for Class Ammo
print(Ammo1.throw_ammo())
print(Ammo1)
print(Ammo1.get_ammo(15))
print(Ammo1.ammo_quantity())



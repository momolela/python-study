# 基类：角色
class Character:
    def __init__(self, name, health, attack_power):
        # 封装：使用双下划线前缀实现私有属性
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    # 封装：提供公共方法访问私有属性
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    def get_attack_power(self):
        return self.__attack_power

    def attack(self, target):
        # 多态：不同角色可能有不同的攻击实现
        damage = self.__attack_power
        print(f"{self.__name} 对 {target.get_name()} 造成了 {damage} 点伤害")
        target.set_health(target.get_health() - damage)

    def display_status(self):
        print(f"{self.__name} 的生命值: {self.__health}")


# 武器类（用于多重继承）
class Weapon:
    def __init__(self, weapon_name, weapon_damage):
        self.weapon_name = weapon_name
        self.weapon_damage = weapon_damage

    def use_weapon(self):
        return self.weapon_damage


# 战士类：继承自 Character
class Warrior(Character):
    def __init__(self, name):
        # 调用父类构造函数
        super().__init__(name, health=100, attack_power=20)
        self.__defense = 10

    def defend(self):
        print(f"{self.get_name()} 开启防御姿态，获得 {self.__defense} 点临时护甲")

    # 方法重写（多态）
    def attack(self, target):
        print(f"战士 {self.get_name()} 挥舞大剑！")
        super().attack(target)

    # 重载方法
    def __str__(self):
        return f"{self.get_name()} 是一个战士，生命值: {self.get_health()}，基础攻击伤害: {self.get_attack_power()}，护甲: {self.__defense}"


# 法师类：继承自 Character
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30)
        self.__mana = 100

    def cast_spell(self):
        if self.__mana >= 20:
            self.__mana -= 20
            print(f"{self.get_name()} 释放火球术！")
            return True
        else:
            print(f"{self.get_name()} 法力不足！")
            return False

    # 方法重写（多态）
    def attack(self, target):
        if self.cast_spell():
            super().attack(target)

    # 重载方法
    def __str__(self):
        return f"{self.get_name()} 是一个法师，生命值: {self.get_health()}，基础攻击伤害: {self.get_attack_power()}"


# 武器战士：多重继承示例
class WeaponWarrior(Warrior, Weapon):
    def __init__(self, name, weapon_name):
        Warrior.__init__(self, name)
        Weapon.__init__(self, weapon_name, weapon_damage=15)

    # 方法重写（多态）
    def attack(self, target):
        print(f"武器战士 {self.get_name()} 使用 {self.weapon_name}！")
        damage = self.use_weapon() + 10  # 基础伤害 + 武器伤害
        print(f"{self.get_name()} 对 {target.get_name()} 造成了 {damage} 点伤害")
        target.set_health(target.get_health() - damage)

    # 重载方法
    def __str__(self):
        return f"{self.get_name()} 是一个武器战士，武器: {self.weapon_name}，生命值: {self.get_health()}，基础攻击伤害: {self.get_attack_power()}，武器伤害: {self.weapon_damage}"


# 测试多态
def battle(attacker, defender):
    attacker.attack(defender)
    defender.display_status()


# 创建对象并测试
if __name__ == "__main__":
    # 创建不同类型的角色
    print("=== 创建不同类型的角色 ===")
    warrior = Warrior("雷欧")
    print(warrior)
    mage = Mage("艾莎")
    print(mage)
    weapon_warrior = WeaponWarrior("亚瑟", "圣剑")
    print(weapon_warrior)

    print("\n=== 测试继承和多态 ===")
    battle(warrior, mage)  # 战士攻击法师
    battle(mage, warrior)  # 法师攻击战士
    battle(weapon_warrior, warrior)  # 武器战士攻击战士

    print("\n=== 测试多重继承 ===")
    print(f"武器战士 {weapon_warrior.get_name()} 的武器: {weapon_warrior.weapon_name}")
    weapon_warrior.defend()  # 调用从 Warrior 继承的方法

    print("\n=== 测试封装 ===")
    # 直接访问私有属性会报错
    # print(warrior.__health)  # 错误：'Warrior' object has no attribute '__health'
    # 通过公共方法访问
    print(f"{warrior.get_name()} 的生命值: {warrior.get_health()}")
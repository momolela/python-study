import tkinter as tk
import random


class SnakeGame:
    def __init__(self, width=600, height=400, block_size=20):
        # 游戏基本设置
        self.width = width
        self.height = height
        self.block_size = block_size
        self.speed = 150  # 游戏速度（毫秒）

        # 初始化游戏窗口
        self.root = tk.Tk()
        self.root.title("贪吃蛇游戏")
        self.root.resizable(False, False)

        # 创建画布
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        # 绑定键盘事件
        self.root.bind("<KeyPress>", self.on_key_press)

        # 初始化游戏变量
        self.reset_game()

    def reset_game(self):
        """重置游戏状态"""
        # 蛇的初始位置和方向
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.next_direction = "Right"

        # 食物位置
        self.food = self.create_food()

        # 游戏状态
        self.score = 0
        self.game_over = False

        # 清除画布并绘制初始状态
        self.canvas.delete("all")
        self.draw_snake()
        self.draw_food()
        self.update_score()

    def create_food(self):
        """随机生成食物位置"""
        while True:
            x = random.randint(1, (self.width - self.block_size) // self.block_size) * self.block_size
            y = random.randint(1, (self.height - self.block_size) // self.block_size) * self.block_size

            # 确保食物不会出现在蛇身上
            if (x, y) not in self.snake:
                return (x, y)

    def draw_snake(self):
        """绘制蛇"""
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x, y, x + self.block_size, y + self.block_size,
                fill="green", outline="black", tags="snake"
            )

    def draw_food(self):
        """绘制食物"""
        x, y = self.food
        self.canvas.create_oval(
            x, y, x + self.block_size, y + self.block_size,
            fill="red", outline="", tags="food"
        )

    def update_score(self):
        """更新分数显示"""
        self.canvas.delete("score")
        self.canvas.create_text(
            50, 15, text=f"分数: {self.score}", fill="white", font=("Arial", 12), tags="score"
        )

        if self.game_over:
            self.canvas.create_text(
                self.width // 2, self.height // 2,
                text="游戏结束！按 R 键重新开始", fill="white",
                font=("Arial", 16, "bold"), tags="game_over"
            )

    def move_snake(self):
        """移动蛇"""
        if self.game_over:
            return

        # 更新方向
        self.direction = self.next_direction

        # 获取蛇头位置
        head_x, head_y = self.snake[0]

        # 根据方向移动蛇头
        if self.direction == "Up":
            head_y -= self.block_size
        elif self.direction == "Down":
            head_y += self.block_size
        elif self.direction == "Left":
            head_x -= self.block_size
        elif self.direction == "Right":
            head_x += self.block_size

        # 检查是否撞到边界
        if (head_x < 0 or head_x >= self.width or
                head_y < 0 or head_y >= self.height):
            self.game_over = True
            self.update_score()
            return

        # 检查是否撞到自己
        if (head_x, head_y) in self.snake:
            self.game_over = True
            self.update_score()
            return

        # 将新头部添加到蛇身
        self.snake.insert(0, (head_x, head_y))

        # 检查是否吃到食物
        if (head_x, head_y) == self.food:
            self.score += 10
            self.food = self.create_food()
            self.draw_food()
            self.update_score()
        else:
            # 如果没吃到食物，移除尾部
            self.snake.pop()

        self.draw_snake()
        self.root.after(self.speed, self.move_snake)

    def on_key_press(self, event):
        """处理键盘输入"""
        key = event.keysym

        # 控制蛇的方向（防止180度转向）
        if (key == "Up" and self.direction != "Down"):
            self.next_direction = "Up"
        elif (key == "Down" and self.direction != "Up"):
            self.next_direction = "Down"
        elif (key == "Left" and self.direction != "Right"):
            self.next_direction = "Left"
        elif (key == "Right" and self.direction != "Left"):
            self.next_direction = "Right"
        elif key == "r" and self.game_over:
            self.reset_game()
            self.move_snake()

    def start(self):
        """开始游戏"""
        self.move_snake()
        self.root.mainloop()


# 启动游戏
if __name__ == "__main__":
    game = SnakeGame()
    game.start()
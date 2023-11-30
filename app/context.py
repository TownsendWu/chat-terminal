class ContextManager:
    """上下文管理器"""

    def __init__(self, initRole="你是一个强大的计算机助手") -> None:
        # 上下文最大字数
        self.maxwordLength = 3000
        self.currentLength = len(initRole)
        self.messages = [
            {"role": "system", "content": initRole},
        ]

    def get(self):
        while self.currentLength >= self.maxwordLength and len(self.messages) > 0:
            content = self.messages[0].get("content", "")
            self.currentLength -= 50 if len(content) == 0 else len(content)
            self.messages = self.messages[1:]

        return self.messages

    def add(self, role, message):
        self.currentLength += len(message)
        self.messages.append({"role": role, "content": message})

    def remove(self, size=1):
        """删最后size个"""
        if len(self.messages) <= 1:
            return

        for _ in range(size):
            del self.messages[-1]

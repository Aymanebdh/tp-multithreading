import numpy as np
import json


class Task:
    def __init__(self, size=1000):
        self.size = size
        self.A = np.random.randn(size, size)
        self.B = np.random.randn(size)
        self.x = None

    def solve(self):
        """Résout A @ x = B"""
        self.x = np.linalg.solve(self.A, self.B)
        return self.A, self.B, self.x

    def to_json(self) -> str:
        """Sérialise l'objet en JSON"""
        # Convertir les tableaux numpy en listes pour JSON
        data = {
            "size": self.size,
            "A": self.A.tolist() if self.A is not None else None,
            "B": self.B.tolist() if self.B is not None else None,
            "x": self.x.tolist() if self.x is not None else None,
        }
        return json.dumps(data)

    @staticmethod
    def from_json(text: str) -> "Task":
        """Crée un Task à partir de JSON"""
        data = json.loads(text)
        task = Task(data["size"])

        # Reconstruire les tableaux numpy
        if data["A"] is not None:
            task.A = np.array(data["A"])
        if data["B"] is not None:
            task.B = np.array(data["B"])
        if data["x"] is not None:
            task.x = np.array(data["x"])

        return task

    def __eq__(self, other: "Task") -> bool:
        """Compare deux objets Task"""
        if not isinstance(other, Task):
            return False

        # Comparer la taille
        if self.size != other.size:
            return False

        # Comparer les matrices avec tolérance numérique
        try:
            if self.A is not None and other.A is not None:
                if not np.allclose(self.A, other.A, rtol=1e-7, atol=0):
                    return False
            elif self.A != other.A:  # Si l'un est None et pas l'autre
                return False

            if self.B is not None and other.B is not None:
                if not np.allclose(self.B, other.B, rtol=1e-7, atol=0):
                    return False
            elif self.B != other.B:
                return False

            if self.x is not None and other.x is not None:
                if not np.allclose(self.x, other.x, rtol=1e-7, atol=0):
                    return False
            elif self.x != other.x:
                return False

            return True
        except ValueError:
            return False


if __name__ == "__main__":
    # Petit test rapide
    t = Task(5)
    t.solve()
    json_str = t.to_json()
    print(f"JSON généré ({len(json_str)} caractères):")
    print(json_str[:100] + "..." if len(json_str) > 100 else json_str)

    t2 = Task.from_json(json_str)
    print(f"\nÉgalité: {t == t2}")

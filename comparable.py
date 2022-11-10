from typing import Protocol, Any


class SupportsLessThan(Protocol):   # Протокол является подклассом typing.Protocol .
        def __lt__(self, other: Any) -> bool: ...   # В теле протокола имеется одно или несколько определений методов,
                                                    # содержащих вместо тела многоточие

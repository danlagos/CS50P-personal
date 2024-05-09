class Jar:
    def __init__(self, capacity=12):
        """
        Initialize the jar with a specified capacity.

        :param capacity: The maximum number of cookies the jar can hold, default is 12.
        :type capacity: int
        :raises ValueError: If the input capacity is not a non-negative integer, with the message 'Capacity must be a non-negative integer.'
        :ivar size: The current number of cookies in the jar, initially set to 0.
        :vartype size: int
        """
        ...

    def __str__(self):
        """
        Return a string representation of the jar.

        Uses the cookie emoji to visually represent each cookie in the jar.

        :return: A string of cookie emojis equal to the current number of cookies in the jar.
        :rtype: str
        """
        ...

    def deposit(self, n):
        """
        Add n cookies to the jar.

        :param n: Number of cookies to add.
        :type n: int
        :raises ValueError: If adding n cookies exceeds the jar's capacity, with the message 'Capacity exceeded.'
        """
        ...

    def withdraw(self, n):
        """
        Remove n cookies from the jar.

        :param n: Number of cookies to remove.
        :type n: int
        :raises ValueError: If attempting to remove more cookies than are currently in the jar, with the message 'Insufficient cookies.'
        """
        ...

    @property
    def capacity(self):
        """
        Provide read-only access to the jar's capacity.

        :return: The maximum capacity of the jar.
        :rtype: int
        """
        ...

    @property
    def size(self):
        """
        Provide read-only access to the current size of the jar.

        Ensures that modifications to size can only occur via the deposit() and withdraw() methods.

        :return: The current number of cookies in the jar.
        :rtype: int
        """
        ...

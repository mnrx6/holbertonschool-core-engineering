#!/usr/bin/env python3
"""This module defines animal classes."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Represent an abstract animal."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Represent a dog."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Represent a cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
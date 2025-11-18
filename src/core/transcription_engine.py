"""
Motor de Transcripción Braille

Este módulo contiene la lógica principal para transcribir texto español a Braille,
siguiendo las reglas del sistema Braille Español.
"""

from typing import List
from src.data.braille_mappings import BrailleMappings


class BrailleTranscriptionEngine:
    """Motor principal de transcripción de texto español a Braille."""
    
    def __init__(self):
        """Inicializa el motor de transcripción con los mapeos necesarios."""
        self._alphabet = BrailleMappings.get_alphabet_mapping()
        self._numbers = BrailleMappings.get_number_mapping()
        self._punctuation = BrailleMappings.get_punctuation_mapping()
        self._number_sign = BrailleMappings.NUMBER_SIGN
    
    def transcribe(self, text: str) -> str:
        """
        Transcribe un texto completo de español a Braille.
        
        Args:
            text (str): Texto en español a transcribir
            
        Returns:
            str: Texto transcrito a Braille
            
        Raises:
            ValueError: Si el texto contiene caracteres no soportados
        """
        if not text:
            return ""
        
        result_chars: List[str] = []
        i = 0
        
        while i < len(text):
            char = text[i]
            
            # Procesar números (pueden ser múltiples dígitos)
            if char.isdigit():
                number_sequence = self._process_number_sequence(text, i)
                result_chars.append(number_sequence)
                # Avanzar el índice por todos los dígitos procesados
                while i < len(text) and text[i].isdigit():
                    i += 1
                continue
            
            # Procesar letras
            if char.lower() in self._alphabet:
                result_chars.append(self._alphabet[char.lower()])
            # Procesar signos de puntuación
            elif char in self._punctuation:
                result_chars.append(self._punctuation[char])
            # Procesar mayúsculas (en Braille español se ignoran o se marca con signo especial)
            elif char.isupper() and char.lower() in self._alphabet:
                result_chars.append(self._alphabet[char.lower()])
            else:
                raise ValueError(f"Carácter no soportado: '{char}'")
            
            i += 1
        
        return ''.join(result_chars)
    
    def _process_number_sequence(self, text: str, start_index: int) -> str:
        """
        Procesa una secuencia de números según las reglas Braille.
        
        El signo de número solo se coloca al principio de la secuencia.
        
        Args:
            text (str): Texto completo
            start_index (int): Índice donde comienza la secuencia numérica
            
        Returns:
            str: Secuencia de números en Braille con el signo de número
        """
        braille_numbers = [self._number_sign]
        
        i = start_index
        while i < len(text) and text[i].isdigit():
            digit = text[i]
            braille_numbers.append(self._numbers[digit])
            i += 1
        
        return ''.join(braille_numbers)
    
    def is_character_supported(self, char: str) -> bool:
        """
        Verifica si un carácter es soportado por el sistema.
        
        Args:
            char (str): Carácter a verificar
            
        Returns:
            bool: True si el carácter es soportado, False en caso contrario
        """
        return (char.lower() in self._alphabet or 
                char in self._punctuation or 
                char.isdigit())
    
    def get_unsupported_characters(self, text: str) -> List[str]:
        """
        Identifica caracteres no soportados en un texto.
        
        Args:
            text (str): Texto a analizar
            
        Returns:
            List[str]: Lista de caracteres no soportados (sin duplicados)
        """
        unsupported = set()
        
        for char in text:
            if not self.is_character_supported(char):
                unsupported.add(char)
        
        return sorted(list(unsupported))

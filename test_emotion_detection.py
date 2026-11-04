"""
Unit tests for the Emotion Detection application.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test suite for EmotionDetection package.
    """

    def test_joy(self):
        """Test dominant emotion joy for 'I am glad this happened'"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """Test dominant emotion anger for 'I am really angry about this'"""
        result = emotion_detector("I am really angry about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """Test dominant emotion disgust for 'I feel disgusted just thinking about it'"""
        result = emotion_detector("I feel disgusted just thinking about it")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """Test dominant emotion sadness for 'I am so sad about this'"""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """Test dominant emotion fear for 'I am afraid this will happen'"""
        result = emotion_detector("I am afraid this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()


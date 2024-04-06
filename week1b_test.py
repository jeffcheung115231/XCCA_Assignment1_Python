import pytest
from week1 import editor
## dont change anything!!!
def test_story1():
	new_text, top_five = editor('data/story.txt')
	expected=['the','of','and','with','a']
	assert set(top_five)==set(expected)
	assert new_text == '''the man and his wife, talking of the latest armed robbery in the suburb, were distracted by the sight of the little boy's pet cat effortlessly arriving over the seven-foot wall, descending first with a rapid bracing of extended forepaws down on the sheer vertical surface, and then a graceful launch, landing with swishing tail within the property.'''

from nose.tools import *
from ex48.parser import *


def test_peek_valid():
    sentence = [('noun', 'bear'), ('verb', 'eats'), ('noun', 'honey')]
    assert_equal('noun', peek(sentence))


def test_peek_invalid():
    sentence = []
    assert_equal(None, peek(sentence))


def test_match_valid():
    sentence = [('noun', 'bear'), ('verb', 'eats'), ('noun', 'honey')]
    assert_equal(match(sentence, 'noun'), ('noun', 'bear'))


def test_match_invalid():
    sentence = [('verb', 'eats'), ('noun', 'honey')]
    assert_is_none(match(sentence, 'noun'))


def test_match_invalid_word_list_none():
    assert_is_none(match(None, 'noun'))


# def test_skip():
#     sentence = [('skip', 'the'), ('noun', 'honey')]
#     test_sentence = [('noun', 'honey')]
#     skip(sentence, 'stop')
#     assert_list_equal(sentence, test_sentence)
def test_parse_verb_valid():
    sentence = [('stop', 'the'),('verb', 'eats')]
    assert_tuple_equal(parse_verb(sentence), ('verb', 'eats'))


def test_parse_verb_invalid():
    sentence = [('stop', 'the'),('noun', 'bear')]
    assert_raises(ParserError,parse_verb, sentence)


def test_parse_object_valid():
    sentence = [('stop', 'the'),('noun', 'princess')]
    assert_tuple_equal(parse_object(sentence), ('noun', 'princess'))


def test_parse_object_invalid():
    sentence = [('stop', 'the'),('stop', 'a')]
    assert_raises(ParserError, parse_object, sentence)


def test_parse_subject_valid():
    sentence = [('stop', 'the'),('noun', 'bear')]
    assert_tuple_equal(parse_subject(sentence), ('noun', 'bear'))


def test_parse_verb_invalid():
    sentence = [('stop', 'the'),('stop', 'a')]
    assert_raises(ParserError,parse_subject, sentence)


def test_parse_sentence():
    sentence_obj = Sentence(('noun', 'bear'), ('verb', 'eats'), ('noun', 'honey'))
    assert_equal(str(sentence_obj), "bear eats honey")

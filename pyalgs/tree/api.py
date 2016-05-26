#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author igor
# Created by iFantastic on 16-5-26
'''
TREE API
abstract base class
'''

ERROR = NotImplementedError("must be implemented by subclass")


class Tree:
    '''
    Abstract base class representing a tree structure
    '''

    # --------------- nested Position class ---------------
    class Position:
        '''
        An abstraction representing the location of a single element
        '''

        def element(self):
            '''
            :return: the element stored as the Position.
            '''
            raise ERROR

        def __eq__(self, other):
            '''
            Returen True if other Positon represents the same location
            '''
            raise ERROR

        def __ne__(self, other):
            '''
            Returen True if other Positon does not represents the same location
            '''

    # ---------abstract methods that concrete subclass must support-------
    def root(self):
        '''
        :return:Position representing the tree's root
        '''
        raise ERROR

    def parent(self, p):
        '''
        :return:Position representing the tree's parent
        '''
        raise ERROR

    def num_children(self, p):
        '''
        :return:Return the number of children that Position p has
        '''
        raise ERROR

    def children(self, p):
        '''
        :return Generate an iteration of Positions representing p's children
        '''
        raise ERROR

    def __len__(self):
        '''
        :return:total number of elements in the tree
        '''
        raise ERROR

    # ------- concrete methods implemented in this class -----
    def is_root(self, p):
        '''
        :return: True if Position p represents the root of the tree
        '''
        return self.root() == p

    def is_learf(self, p):
        '''
        :return: True if Position p does not have any children
        '''
        return self.num_children(p) == 0

    def is_empty(self):
        '''
        :return:True if the tree is empty
        '''
        return len(self) == 0

    def depth(self, p):
        '''
        :return:the number of levels separating Position p from the root
        '''
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        '''
        if p is a leaf,then the height of p is 0
        Otherwise,the height of p is one more than the maximum of the heights of p's children
        '''
        if self.is_learf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        '''
        Return the height of the subtree rooted at Position p
        if p is None,return the height of the entire tree
        '''
        if p is None:
            p = self.root()
        return self._height(p)



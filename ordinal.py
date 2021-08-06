"""
Author: ZR000X
Dated: 2021-08-06
License: MIT
Source: https://github.com/ZR000X/Nodes
"""


class Ordinal():
    """
    An ordinal is simply a set of all things it is greater than.
    """
    def __init__(self, subordinates=[], superiors=[], inform_on_init = True) -> None:
        if type(subordinates) is Ordinal:
            self.subordinates = [subordinates]
        else:
            self.subordinates = subordinates
        self.superiors = superiors
        if inform_on_init:
            self.inform_subordinates()
            self.inform_superiors()

    def __ge__(self, other):
        return other in self.subordinates

    def __le__(self, other):
        return self in other.subordinates

    def equals(self, other):
        return self >= other and other >= self

    def get_rank(self, superiors_asking=[]) -> int:
        """
        the rank of an ordinal is precisely one more than the maximum rank of its subordinates
        """
        # deal with empty lists
        if len(self.subordinates) == 0:
            return 0 
        # Loop through subordinates
        confused = False
        equals = []
        result = 0
        for sub in self.subordinates:
            # check that subordinate is not contradictory
            # Note: the original asker can never be confused
            if sub in superiors_asking:
                confused = True
                equals += [sub]
                continue
            # if not, get some return from the subordinate when asking rank
            rank = sub.get_rank(superiors_asking=superiors_asking + [self])
            # assess the return we got from asking rank
            if type(rank) is int:
                if rank >= result:
                    result = rank + 1
            else:
                if rank[0] >= result:
                    result = rank[0]
                equals += rank[1]
                # this subordinate continues the chain of confusion if it answers to superiors
                # if it sees itself in equals, however, it realises not to be confused
                if len(superiors_asking) > 0 and self not in equals:
                    confused = True                
        # decide what to return based on confusion
        if confused:
            return [result, equals]
        return result

    def get_depth(self, subordinates_asking=[]) -> int:
        """
        the depth of an ordinal is precisely one more than the maximum depth of its superiors
        """
        # deal with empty lists
        if len(self.superiors) == 0:
            return 0 
        # Loop through superiors
        confused = False
        equals = []
        result = 0
        for sup in self.superiors:
            # check that superior is not contradictory
            # Note: the original asker can never be confused
            if sup in subordinates_asking:
                confused = True
                equals += [sup]
                continue
            # if not, get some return from the superior when asking rank
            rank = sup.get_depth(subordinates_asking=subordinates_asking + [self])
            # assess the return we got from asking rank
            if type(rank) is int:
                if rank >= result:
                    result = rank + 1
            else:
                if rank[0] >= result:
                    result = rank[0]
                equals += rank[1]
                # this superior continues the chain of confusion if it answers to subordinates
                # if it sees itself in equals, however, it realises not to be confused
                if len(subordinates_asking) > 0 and self not in equals:
                    confused = True                
        # decide what to return based on confusion
        if confused:
            return [result, equals]
        return result

    def hire_subordinate(self, sub, inform_sub: bool = True):
        if inform_sub:
            if self not in sub.superiors:
                sub.superiors.append(self)
        self.subordinates.append(sub)            

    def inform_subordinates(self):
        """
        Ensures all subordinates are aware of their subordination
        """
        if self.subordinates is not None:
            for sub in self.subordinates:
                if type(sub) is not str and self not in sub.superiors:
                    sub.superiors.append(self)

    def inform_all_subordinates(self):
        self.inform_subordinates()
        for sub in self.subordinates:
            sub.inform_all_subordinates()

    def inform_superiors(self):
        """
        Ensures all superiors are aware of their superiority
        """
        if self.superiors is not None:
            for sup in self.superiors:
                if self not in sup.superiors:
                    sup.subordinates.append(self)
    
    def inform_all_superiors(self):
        self.inform_superiors()
        for sup in self.superiors:
            sup.inform_all_superiors()

    def is_root(self):
        return len(self.subordinates) == 0

    def is_peak(self):
        return len(self.superiors) == 0

    def get_roots(self, roots=[]):
        for sub in self:
            if sub is self or sub in roots:
                return []            
            if sub.is_root():
                roots.append(sub)
            else:
                roots += sub.get_roots(roots)
        return roots

    def get_peaks(self, peaks=[]):
        for sup in self.superiors:
            if sup is self or sup in peaks:
                return []            
            if sup.is_peak():
                peaks.append(sup)
            else:
                peaks += sup.get_peaks(peaks)
        return peaks
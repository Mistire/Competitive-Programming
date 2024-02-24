class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights)) 
        
        sortedPeople = sorted(people, key = lambda x: x[1], reverse=True)
        
        person = [people[0] for people in sortedPeople]
        return person


        
        
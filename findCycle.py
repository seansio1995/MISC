def findCycle(firstNode):
    slowRunner=firstNode
    fastRunner=firstNode

    while fastRunner is not None and fastRunner.next is not None:
        fastRunner=fastRunner.next.next
        slowRunner=slowRunner.next

        if fastRunner=slowRunner:
            return True
    return False

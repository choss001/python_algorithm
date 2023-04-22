if __name__ == '__main__':

    def hide_and_seek(n, k):
        # Initialize a visited list to keep track of positions already visited
        visited = [False] * 100001
        queue = [(n, 0, [n])]  # Initialize a queue with Subin's position and time taken to reach that position

        while queue:
            pos, time, trace_array = queue.pop(0)
            if pos == k:
                print(trace_array)
                return time  # If we have reached the sister's position, return the time taken
            if not visited[pos]:
                visited[pos] = True
                if pos > 0:
                    queue.append((pos-1, time+1, [*trace_array, pos-1]))  # Move one step to the left
                if pos < 100000:
                    queue.append((pos+1, time+1, [*trace_array, pos+1]))  # Move one step to the right
                if pos < k and pos * 2 <= 100000:
                    queue.append((pos*2, time, [*trace_array, pos*2]))  # Teleport to position 2*X

    #           print(f'queue = {queue}')
    #           print(f'pos = {pos}, time = {time}')


        return -1  # If we can't reach the sister's position, return -1

    # Example usage:
    print(hide_and_seek(0, 100000))  # Output: 2

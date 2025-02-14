from friendsbalt.acs import MinPQ


class HuffmanEncoding:
    def __init__(self, src=None, encoded_text=None, root=None):
        """
        Initializes a new Huffman Encoding. Either source text or encoded text and root must be provided.
        If source text is provided, it builds the Huffman tree and dictionary, and encodes the text.
        If encoded text and root are provided, it decodes the text.
        Args:
            src (str, optional): The source text to be encoded.
            encoded_text (str, optional): The encoded text to be decoded.
            root (Node, optional): The root node of the Huffman tree for decoding.
        """
        if src is not None:
            self.src = src
            self.tree_root = self._build_tree()
            self.encoded_text = self._encode  
            self.dictiionary = self._build_dictionary       

    




    def _build_tree(self):

        freq = {}

        for letter in self.src:
                freq[letter] = freq.get(letter, 0) + 1
                leaderboard = sorted(freq, key=lambda x: freq[x], reverse=True)
        pq = MinPQ()
        for letter in freq.keys():
                        node = self.Node(freq[letter], char= letter)
                        pq.insert(node)

        while len(pq.size()) > 1:
                leftNode = pq.pop()
                rightNode = pq.pop()
                newNode = self.Node(leftNode.freq + rightNode.freq, left=leftNode, right=rightNode)
                pq.insert(newNode)
         
    
    class Node:
        def __init__(self, freq, char=None, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right
        
        def is_leaf(self):
            return self.char is not None

    def encoding(self):
        """
        Returns the encoded text.
        Returns:
            str: The encoded text as a string of 0s and 1s.
        """
        dict = {}

        for char in self.src:
                 dict.append(self.dictionary[char])
        return '' .join(dict)

             
        

    def source_text(self):
        """
        Returns the original source text.
        Returns:
            str: The original source text.
        """
        pass

    def root(self):
        """
        Returns the root node of the Huffman tree.
        Returns:
            Node: The root node of the Huffman tree.
        """
       
    
    def _build_dictionary(self, node=None, prefix=''):
        """
        Recursively builds a dictionary that maps characters to their corresponding
        Huffman codes based on the Huffman tree.
        Args:
            node (Node, optional): The current node in the Huffman tree. Defaults to None,
                                   which means the function will start from the root node.
            prefix (str, optional): The current Huffman code prefix. Defaults to an empty string.
        Returns:
            dict: A dictionary where keys are characters and values are their corresponding
                  Huffman codes.
        """
        if node is None:
            node = self.root
        
        if node.char is not None:
            return {node.char: prefix}
        
        dictionary = {}
        dictionary.update(self._build_dictionary(node.left, prefix + '0'))
        dictionary.update(self._build_dictionary(node.right, prefix + '1'))
        return dictionary
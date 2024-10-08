def decode_message( s: str, p: str) -> bool:
        if len(s) != len(p):
                return False
        pattern_to_str = {}
        str_to_pattern = {}

        for char_p, char_s in zip(p,s):
                if char_p in pattern_to_str:
                        if pattern_to_str[char_p] != char_s:
                                return False
                        

                else:
                        pattern_to_str[char_p] = char_s
        
        if char_s in str_to_pattern:
                if str_to_pattern[char_s] != char_p:
                        return False
        else:
                str_to_pattern[char_s] = [char_p]
        return True
                
                
        






# constant

class Morph:
    MORPH = {   # 명사
                'NNG': 'NOUN', 'NNP': 'NOUN', 'NNB': 'NOUN', 'NR': 'NOUN','NF': 'NOUN', 'NP': 'NOUN',
                # 용언
                'VV': 'VERB', 'VA': 'VERB', 'VX': 'VERB', 'VCP': 'VERB','VCN': 'VERB', 'NV': 'VERB',
                # 관형사
                'MM': 'DETER',
                # 부사
                'MAG': 'ADVERB', 'MAJ': 'ADVERB',
                # 감탄사
                'IC': 'EXCLAM',
                # 조사
                'JKS': 'POST','JKC': 'POST', 'JKG': 'POST', 'JKO': 'POST', 'JKB': 'POST', 'JKV': 'POST',
                'JKQ': 'POST', 'JX': 'POST', 'JC': 'POST',
                # 어미
                'EP': 'END','EF': 'END','EC': 'END','ETN': 'END','ETM': 'END',
                # 접사
                'XPN': 'AFFIX','XSN': 'AFFIX','XSV': 'VERB','XSA': 'AFFIX', 'XR': 'AFFIX',
                # 부호
                'SF': 'MARK','SP': 'MARK','SS': 'MARK','SE': 'MARK','SO': 'MARK','SW': 'MARK',
                # 숫자
                'SN': 'NUMBER',
                # 외국어, 한자 제외
                'SL': 'IGNORE','SH': 'IGNORE',
                # 분석 불능 범주 제외
                'NA': 'IGNORE'
    }

    USE_POST = ['랑','에서','더러','보다','에게', '의', '로', '이라고', '에', '처럼','께','으로','한테',  # 격조사
                '이나','든지','부터','도','커녕','마다','밖에','뿐','만','까지',                      # 보조사
                '과','와','이랑',                                                                                    # 접속조사
                '이니까','이다']                                                                              # 서술격 조사


    USE_END = ['았','었','ㅂ시다','면서','자','지만','던','면','러','다오','ㅂ니까','다가']

    SPECIAL_NOUN = {'꺼': '것', '뭐': '무엇', '거': '것'}
    SPECIAL_END = {'았': '끝', '었': '끝'}
    SPECIAL_AFFIX = {'스럽': '하다', '하': '하다'}

pass


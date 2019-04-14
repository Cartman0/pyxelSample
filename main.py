import pyxel
from collections import namedtuple


class App:
    """
    - フレームレートごとに文字色変更
    - qを押すと終了

    http://tkitao.hatenablog.com/entry/2018/11/24/185346

    blt(x, y, img, u, v, w, h, [colkey])
    イメージバンクimg(0-2) の (u, v) からサイズ (w, h) の領域を (x, y) にコピーする。w、hそれぞれに負の値を設定すると水平、垂直方向に反転する。colkeyに色を指定すると透明色として扱われる

    """

    def __init__(self):
        pyxel.init(128, 128, caption="Hello Pyxel", scale=4, fps=60)
        pyxel.image(0).load(0, 0, "pyxel_logo_38x16.png")
        print(dir(pyxel.image(0)))
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        # text(x, y, s, col) 色colの文字列sを (x, y) に描画する
        pyxel.text(
            0, 0, f"Hello, Pyxel! {pyxel.frame_count}", pyxel.frame_count % 16)
        pyxel.text(0, 16, "あアァ亜Aa", 15)  # アルファベットのみ
        # blt(x, y, img, u, v, w, h, [colkey])
        u = pyxel.image(0).width
        v = pyxel.image(0).height
        # print(v)
        center = self._centering(128, 128, 38, 16)
        pyxel.blt(center.x, center.y, 0, 0, 0, center.u, center.v)

    def _centering(self, overall_x, overall_y, view_w, view_h):
        Pos = namedtuple('Pos', 'x, y, u, v')
        return Pos(x=overall_x/2 - view_w/2, y=overall_y / 2 - view_h/2, u=view_w, v=view_h)


App()

from manim import *


class ReduceRationalFraction(Scene):

	def construct(self) -> None:
		# Исходная дробь
		original_fraction = MathTex(r"\frac{6x^2\,y}{9x\,y^2}")
		title = Text("Сокращение рациональных дробей", font_size=36)
		title.to_edge(UP)
		self.play(FadeIn(title, shift=UP*0.3))
		self.play(Write(original_fraction))
		self.wait(0.8)

		# Факторизация с пометкой общих множителей зелёным
		# Помечаем РОВНО те множители, которые будем сокращать.
		# В числителе из x^2 оставляем один x не помеченным, второй x помечаем как общий.
		factored = MathTex(
			# numerator
			r"\frac{2\cdot \color{#12b886}{3}\cdot x\cdot \color{#12b886}{x}\cdot \color{#12b886}{y}""
			# denominator
			r"}{\color{#12b886}{3}\cdot \color{#12b886}{x}\cdot \color{#12b886}{y}\cdot y}"
		)
		factored.next_to(title, DOWN, buff=1.0)

		# Подсказки
		hint1 = Text("Разложим на множители и выделим общие", font_size=28)
		hint1.next_to(factored, DOWN, buff=0.6)

		self.play(TransformMatchingTex(original_fraction, factored))
		self.play(FadeIn(hint1, shift=DOWN*0.2))
		self.wait(0.6)

		# Функция для рисования красной диагональной черты по объекту (зачёркивание)
		def strike_through(mob: VMobject, color: Color = RED, scale: float = 1.15) -> Line:
			ul = mob.get_corner(UL)
			dr = mob.get_corner(DR)
			center = mob.get_center()
			vec = dr - ul
			line = Line(ul, dr)
			line.set_color(color)
			line.set_stroke(width=6)
			line.scale(scale, about_point=center)
			return line

		# Находим части, которые были помечены зелёным: 3, x, y (один из каждого в числителе и знаменателе)
		# Мы специально раскрасили только те экземпляры, которые сокращаются, поэтому можно зачёркивать все зелёные
		colored_parts: list[VMobject] = []
		for part in factored.family_members_with_points():
			if isinstance(part, VMobject) and part.get_stroke_color() == Color("#12b886") or part.get_color() == Color("#12b886"):
				colored_parts.append(part)

		# Для стабильности уберём дубликаты (вложенные субмобы) и оставим верхние глифы
		unique_parts: list[VMobject] = []
		for p in colored_parts:
			if all(p not in q.family_members_with_points() for q in colored_parts if q is not p):
				unique_parts.append(p)

		strikes = VGroup(*[strike_through(p) for p in unique_parts])
		self.play(LaggedStart(*[Create(s) for s in strikes], lag_ratio=0.1), run_time=1.2)
		self.wait(0.4)

		# Небольшое приглушение зачёркнутых множителей
		fade_anims = []
		for p in unique_parts:
			fade_anims.append(p.animate.set_opacity(0.2))
		self.play(*fade_anims, run_time=0.6)
		self.wait(0.2)

		# Переход к результату
		result = MathTex(r"\frac{2x}{3y}")
		result.move_to(factored)
		hint2 = Text("После сокращения", font_size=28)
		hint2.next_to(result, DOWN, buff=0.6)
		self.play(FadeOut(hint1, shift=DOWN*0.2))
		self.play(FadeOut(strikes, lag_ratio=0.05, run_time=0.6))
		self.play(TransformMatchingTex(factored, result))
		self.play(FadeIn(hint2, shift=DOWN*0.2))
		self.wait(1.2)

		# Завершение
		self.play(*[FadeOut(m) for m in self.mobjects])


# Подсказки по запуску (CLI):
#   1) Установите зависимости (пример для Debian/Ubuntu):
#      sudo apt-get update && sudo apt-get install -y ffmpeg texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended dvisvgm
#      python3 -m pip install -U manim
#   2) Рендер (низкое качество, быстро):
#      manim -pql /workspace/manim_fraction.py ReduceRationalFraction
#      (файл видео появится в папке media/)


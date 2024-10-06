from manim import *


class ProjectVideo(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def animate_path(self, points):
        person = Star(outer_radius=0.2, color=BLACK).set_fill(YELLOW, opacity=1)
        person.z_index = 1
        person.move_to(points[0])
        self.add(person)
        lines = []
        for i in range(1, len(points)):
            lines.append(Line(points[i - 1], points[i]).set_stroke(YELLOW, width=3))
            self.play(Create(lines[i-1]), person.animate.move_to(points[i]))
        for line in lines:
            self.remove(line)
        self.remove(person)

    def draw_paths(self):
        d = 3.58
        left2=-1.30 + d
        left1=-0.4 + d
        right=1.4 + d
        right2=2.2 + d
        up=1.35
        down=-1.35
        p1 = [left2, up, 0]
        p2 = [left2, 0, 0]
        p3 = [left2, down, 0]

        p4 = [left1, up, 0]
        p5 = [left1, 0, 0]
        p6 = [left1, down, 0]

        p7 = [right, up, 0]
        p8 = [right2, 0, 0]
        p9 = [right, down, 0]

        line_1_points = [p3, p1, p4, p5, p8, p9, p6, p5]
        self.animate_path(line_1_points)

        line_2_points = [p7, p8, p9, p3, p1, p4, p6]
        self.animate_path(line_2_points)

        line_3_points = [p8, p7, p4, p5, p8, p9, p3, p1]
        self.animate_path(line_3_points)


    def create_map(self):

        vg = VGroup()
        background = Rectangle(height=4, width=6).set_color(GREEN_D)
        background.set_fill(GREEN_D, opacity=1)
        vg.add(background)

        river = Rectangle(height=2, width=6).set_color(BLUE).set_fill(BLUE, opacity=1)
        vg.add(river)

        island = RoundedRectangle(width=3, height=1.3, corner_radius=0.2) \
            .set_fill(GREEN_D, opacity=1).set_stroke(GREEN_D).shift(0.9*LEFT)
        island2 = RoundedRectangle(width=2, height=1.3, corner_radius=0.2) \
            .set_fill(GREEN_D, opacity=1).set_stroke(GREEN_D).align_to(background, RIGHT)
        island2_5 = Rectangle(width=1, height=1.3) \
            .set_fill(GREEN_D, opacity=1).set_stroke(GREEN_D).align_to(background, RIGHT)
        vg.add(island, island2, island2_5)



        bridge1 = Rectangle(height=0.7, width=0.3).set_fill(DARK_BROWN, opacity=1).set_stroke(DARK_BROWN).shift(1.3*LEFT + 0.8*DOWN)
        bridge2 = Rectangle(height=0.7, width=0.3).set_fill(DARK_BROWN, opacity=1).set_stroke(DARK_BROWN).shift(0.4*LEFT + 0.8*DOWN)
        bridge3 = Rectangle(height=0.7, width=0.3).set_fill(DARK_BROWN, opacity=1).set_stroke(DARK_BROWN).shift(1.3*LEFT + 0.8*UP)
        bridge4 = Rectangle(height=0.7, width=0.3).set_fill(DARK_BROWN, opacity=1).set_stroke(DARK_BROWN).shift(0.4*LEFT + 0.8*UP)
        bridge5 = Rectangle(height=0.7, width=0.3).set_fill(DARK_BROWN, opacity=1).set_stroke(DARK_BROWN).shift(1.7*RIGHT + 0.8*DOWN)
        bridge6 = Rectangle(height=0.7, width=0.3).set_fill(DARK_BROWN, opacity=1).set_stroke(DARK_BROWN).shift(1.7*RIGHT + 0.8*UP)
        bridge7 = Rectangle(height=0.3, width=0.7).set_fill(DARK_BROWN, opacity=1).set_stroke(DARK_BROWN).shift(0.8*RIGHT)
        bridge5.rotate(-30*DEGREES)
        bridge6.rotate(30*DEGREES)
        vg.add(bridge1, bridge2, bridge3, bridge4, bridge5, bridge6, bridge7)


        return vg

    def create_graph1(self):
        vertices = [1, 2, 3, 4]

        left = 3.2
        right = 5.7
        up = 1.7
        center = 0
        down = -1.7
        lt = {1: [left, up, 1], 2: [right, center, 1], 3: [left, down, 1], 4: [left, center, 1]}


        edges = [(3, 4), (1, 4), (2, 4)]
        G = Graph(vertices, edges, edge_type=Line, layout=lt)

        G.add_edges((2, 1), edge_type=ArcBetweenPoints, edge_config={"angle": PI/2})
        G.add_edges((3, 2), edge_type=ArcBetweenPoints, edge_config={"angle": PI/2})
        G.add_edges((4, 3), edge_type=ArcBetweenPoints, edge_config={"angle": 13*PI/12})
        G.add_edges((1, 4), edge_type=ArcBetweenPoints, edge_config={"angle": 13*PI/12})
        self.play(Create(G))
        self.wait()


        return G


    def create_graph2(self):
        vertices = [1, 2, 3, 4]

        left = 3.5
        right = 5.5
        up = 1
        center = 4.5
        down = -1
        lt = {1: [center, up, 1], 2: [right, 0, 1], 3: [center, down, 1], 4: [left, 0, 1]}


        edges = [(3, 4), (1, 4), (2, 4), (2, 1), (3, 2)]
        G = Graph(vertices, edges, edge_type=Line, layout=lt)
        G.add_edges((4, 3), edge_type=ArcBetweenPoints, edge_config={"angle": PI/2})
        G.add_edges((1, 4), edge_type=ArcBetweenPoints, edge_config={"angle": PI/2})
        return G


    def normalize_graph(self, G1):

        '''
        self.play(G[1].animate.move_to([4.5, 2, 0]),
                  G[2].animate.move_to([5.5, 0, 0]),
                  G[3].animate.move_to([4.5, -2, 0]),
                  G[4].animate.move_to([3.5, 0, 0])
                  )
        '''
        G2 = self.create_graph2()
        self.play(ReplacementTransform(G1, G2, run_time=1))
        self.wait()


    def euler_text(self):

        text1 = Text('Eulervei: \nEn vei som går gjennom \nhver kant nøyaktig 1 gang.', color=BLUE).scale(0.8).to_edge(LEFT)
        self.add(text1)

    def create_curve(self, start_x, start_y, stop_x, stop_y, offset):
        curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
        new_curve = CurvesAsSubmobjects(curve)


    def construct(self):
        #self.camera.background_color = BLUE
        #self.wait(0.5)  # wait for 0.5 seconds
        #bridges.height = 2
        #self.add(bridges)
        text = Text('De 7 broene av Königsberg').scale(1).shift(UP*3)
        self.add(text)

        map = self.create_map()
        self.add(map)
        self.wait(1)
        self.play(map.animate.to_edge(RIGHT))
        self.euler_text()
        self.draw_paths()


        graph = self.create_graph1()
        self.play(FadeOut(map.set_z_index(-1)))
        self.normalize_graph(graph)


        self.transform()




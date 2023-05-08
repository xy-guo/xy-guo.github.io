import jinja2
from dataclasses import dataclass
from typing import List

title = 'Xiaoyang Guo - CUHK'
name = 'Xiaoyang Guo'

author_links = {
    "Shaoshuai Shi": "https://shishaoshuai.com/",
    "Hongsheng Li": "https://www.ee.cuhk.edu.hk/~hsli/",
    "Xiaogang Wang": "https://www.ee.cuhk.edu.hk/~xgwang/",
    "Kai Yang": "https://scholar.google.com/citations?user=s5Z6X0cAAAAJ&hl=en",
    "Hongyang Li": "https://lihongyang.info/",
    "Bo Dai": "https://daibo.info/",
    "Wanli Ouyang": "https://wlouyang.github.io/",
    "Shuai Yi": "https://scholar.google.com/citations?user=afbbNmwAAAAJ&hl=zh-CN",
    "Jimmy Ren": "http://www.jimmyren.com/"
}


@dataclass
class Author:
    name: str
    url: str


@dataclass
class Paper:
    title: str
    conference: str
    year: int
    authors: List[Author]
    url: str
    url_arxiv: str
    url_project_page: str = None
    url_paper: str = None
    url_supp: str = None
    url_video: str = None
    url_poster: str = None
    url_code: str = None
    description: str = None
    image: str = None
    special_honor: str = None


def gen_author_list(*author_names):
    authors = []
    for author_name in author_names:
        authors.append(Author(
            name=author_name,
            url=author_links.get(author_name, None)
        ))
    return authors


def get_papers():
    papers = []
    papers.append(Paper(
        title="LIGA-Stereo: Learning Lidar Geometry aware Representations for Stereo-based 3d Detector",
        conference="International Conference on Computer Vision (<b>ICCV</b>)",
        year=2021,
        authors=gen_author_list("Xiaoyang Guo", "Shaoshuai Shi", "Xiaogang Wang", "Hongsheng Li"),
        url="https://openaccess.thecvf.com/content/ICCV2021/html/Guo_LIGA-Stereo_Learning_LiDAR_Geometry_Aware_Representations_for_Stereo-Based_3D_Detector_ICCV_2021_paper.html",
        url_arxiv="https://arxiv.org/abs/2108.08258",
        url_paper="https://openaccess.thecvf.com/content/ICCV2021/html/Guo_LIGA-Stereo_Learning_LiDAR_Geometry_Aware_Representations_for_Stereo-Based_3D_Detector_ICCV_2021_paper.html",
        url_supp="https://openaccess.thecvf.com/content/ICCV2021/supplemental/Guo_LIGA-Stereo_Learning_LiDAR_ICCV_2021_supplemental.pdf",
        url_poster=None,
        url_code="https://github.com/xy-guo/LIGA-Stereo",
        image="./images/liga.png",
        special_honor="Ranked 1st place among stereo-based 3D detection methods on KITTI (July 2021), refer to <a href=\"https://www.cvlibs.net/datasets/kitti/eval_object_detail.php?&result=d5d1938b704537150df7f8403d173aa16fe9ba17\">here</a>."
    ))
    papers.append(Paper(
        title="Group-wise Correlation Stereo Network",
        conference="Conference on Computer Vision and Pattern Recognition(<b>CVPR</b>)",
        year=2019,
        authors=gen_author_list("Xiaoyang Guo", "Kai Yang", "Wukui Yang", "Xiaogang Wang", "Hongsheng Li"),
        url="https://openaccess.thecvf.com/content_CVPR_2019/html/Guo_Group-Wise_Correlation_Stereo_Network_CVPR_2019_paper.html",
        url_arxiv="https://arxiv.org/abs/1903.04025",
        url_paper="https://openaccess.thecvf.com/content_CVPR_2019/html/Guo_Group-Wise_Correlation_Stereo_Network_CVPR_2019_paper.html",
        url_poster=None,
        url_code="https://github.com/xy-guo/GwcNet",
        image="./images/gwcnet.jpg",
    ))
    papers.append(Paper(
        title="Unsupervised Cross-Spectral Stereo Matching by Learning to Synthesize",
        conference="AAAI",
        year=2019,
        authors=gen_author_list("Xiaoyang Guo*", "Mingyang Liang*", "Hongsheng Li", "Xiaogang Wang", "You Song"),
        url="https://ojs.aaai.org/index.php/AAAI/article/view/4894",
        url_arxiv="https://arxiv.org/abs/1903.01078",
        url_paper="https://ojs.aaai.org/index.php/AAAI/article/view/4894",
        image="./images/cs-stereo.jpg",
        special_honor="Oral"
    ))
    papers.append(Paper(
        title="Learning Monocular Depth by Distilling Cross-domain Stereo Networks",
        conference="European Conference on Computer Vision(<b>ECCV</b>)",
        year=2018,
        authors=gen_author_list("Xiaoyang Guo", "Hongsheng Li", "Shuai Yi", "Jimmy Ren", "Xiaogang Wang"),
        url="https://openaccess.thecvf.com/content_ECCV_2018/html/Xiaoyang_Guo_Learning_Monocular_Depth_ECCV_2018_paper.html",
        url_arxiv="https://arxiv.org/abs/1808.06586",
        url_paper="https://openaccess.thecvf.com/content_ECCV_2018/html/Xiaoyang_Guo_Learning_Monocular_Depth_ECCV_2018_paper.html",
        url_poster=None,
        url_video="https://www.youtube.com/watch?v=QAcuYT7q_gY",
        url_code="https://github.com/xy-guo/Learning-Monocular-Depth-by-Stereo",
        image="./images/mono.jpg",
    ))
    papers.append(Paper(
        title="Neural Network Encapsulation",
        conference="European Conference on Computer Vision(<b>ECCV</b>)",
        year=2018,
        authors=gen_author_list("Hongyang Li", "Xiaoyang Guo", "Bo Dai", "Wanli Ouyang", "Xiaogang Wang"),
        url="https://openaccess.thecvf.com/content_ECCV_2018/html/Hongyang_Li_Neural_Network_Encapsulation_ECCV_2018_paper.html",
        url_arxiv="https://arxiv.org/abs/1808.03749",
        url_paper="https://openaccess.thecvf.com/content_ECCV_2018/html/Hongyang_Li_Neural_Network_Encapsulation_ECCV_2018_paper.html",
        url_poster=None,
        image="./images/encap.png",
    ))

    return papers

def render_index(filename="index.jinja"):
    render_data = dict(
        title=title,
        name=name,
        papers=get_papers()
    )
    subs = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./')
    ).get_template(filename).render(**render_data)

    with open(filename.replace(".jinja", ".html"), 'w') as f:
        f.write(subs)


if __name__ == "__main__":
    render_index()
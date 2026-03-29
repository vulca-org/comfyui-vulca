"""Basic tests for ComfyUI VULCA nodes (no ComfyUI runtime required)."""
from __future__ import annotations

import sys
import os
import pytest

# Add vulca to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "vulca", "src"))


def test_node_mappings():
    from nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
    assert "VULCABrief" in NODE_CLASS_MAPPINGS
    assert "VULCAConcept" in NODE_CLASS_MAPPINGS
    assert "VULCAEvaluate" in NODE_CLASS_MAPPINGS
    assert "VULCAGenerate" in NODE_CLASS_MAPPINGS
    assert "VULCAUpdate" in NODE_CLASS_MAPPINGS
    assert "VULCAInpaint" in NODE_CLASS_MAPPINGS
    assert "VULCALayersAnalyze" in NODE_CLASS_MAPPINGS
    assert "VULCALayersComposite" in NODE_CLASS_MAPPINGS
    assert "VULCAEvolution" in NODE_CLASS_MAPPINGS
    assert "VULCATraditions" in NODE_CLASS_MAPPINGS
    assert "VULCALayersExport" in NODE_CLASS_MAPPINGS
    assert len(NODE_CLASS_MAPPINGS) == 11
    assert len(NODE_DISPLAY_NAME_MAPPINGS) == 11


def test_brief_node_input_types():
    from nodes import VULCABriefNode
    inputs = VULCABriefNode.INPUT_TYPES()
    assert "required" in inputs
    assert "intent" in inputs["required"]


def test_evaluate_node_return_types():
    from nodes import VULCAEvaluateNode
    assert len(VULCAEvaluateNode.RETURN_TYPES) == 6  # scores_json + L1-L5


def test_brief_node_creates_brief(tmp_path):
    os.environ["VULCA_PROJECT_DIR"] = str(tmp_path)
    from nodes import VULCABriefNode
    node = VULCABriefNode()
    result = node.create_brief("水墨山水", mood="serene")
    assert result[0]  # brief_path
    assert (tmp_path / "brief.yaml").exists()
    del os.environ["VULCA_PROJECT_DIR"]


def test_evaluate_node_mock():
    from nodes import VULCAEvaluateNode
    node = VULCAEvaluateNode()
    result = node.evaluate("nonexistent.jpg", mock=True)
    scores_json, l1, l2, l3, l4, l5 = result
    assert isinstance(l1, float)
    assert isinstance(l5, float)


def test_inpaint_node_input_types():
    from nodes import VULCAInpaintNode
    inputs = VULCAInpaintNode.INPUT_TYPES()
    assert "required" in inputs
    assert "image_path" in inputs["required"]
    assert "region" in inputs["required"]
    assert "instruction" in inputs["required"]
    assert "optional" in inputs
    assert "tradition" in inputs["optional"]
    assert "count" in inputs["optional"]


def test_inpaint_node_return_types():
    from nodes import VULCAInpaintNode
    assert VULCAInpaintNode.RETURN_TYPES == ("STRING", "STRING")
    assert VULCAInpaintNode.RETURN_NAMES == ("blended_path", "variants_json")
    assert VULCAInpaintNode.CATEGORY == "VULCA"


def test_layers_analyze_node_input_types():
    from nodes import VULCALayersAnalyzeNode
    inputs = VULCALayersAnalyzeNode.INPUT_TYPES()
    assert "required" in inputs
    assert "image_path" in inputs["required"]


def test_layers_analyze_node_return_types():
    from nodes import VULCALayersAnalyzeNode
    assert VULCALayersAnalyzeNode.RETURN_TYPES == ("STRING",)
    assert VULCALayersAnalyzeNode.RETURN_NAMES == ("layers_json",)
    assert VULCALayersAnalyzeNode.CATEGORY == "VULCA"


def test_layers_composite_node_input_types():
    from nodes import VULCALayersCompositeNode
    inputs = VULCALayersCompositeNode.INPUT_TYPES()
    assert "required" in inputs
    assert "artwork_dir" in inputs["required"]


def test_layers_composite_node_return_types():
    from nodes import VULCALayersCompositeNode
    assert VULCALayersCompositeNode.RETURN_TYPES == ("STRING",)
    assert VULCALayersCompositeNode.RETURN_NAMES == ("composite_path",)
    assert VULCALayersCompositeNode.CATEGORY == "VULCA"


def test_display_names():
    from nodes import NODE_DISPLAY_NAME_MAPPINGS
    assert NODE_DISPLAY_NAME_MAPPINGS["VULCAInpaint"] == "VULCA Inpaint (Region)"
    assert NODE_DISPLAY_NAME_MAPPINGS["VULCALayersAnalyze"] == "VULCA Layers (Analyze)"
    assert NODE_DISPLAY_NAME_MAPPINGS["VULCALayersComposite"] == "VULCA Layers (Composite)"
    assert NODE_DISPLAY_NAME_MAPPINGS["VULCAEvolution"] == "VULCA Evolution (Status)"
    assert NODE_DISPLAY_NAME_MAPPINGS["VULCATraditions"] == "VULCA Traditions (List)"
    assert NODE_DISPLAY_NAME_MAPPINGS["VULCALayersExport"] == "VULCA Layers (Export)"


def test_evolution_node_input_types():
    from nodes import VULCAEvolutionNode
    inputs = VULCAEvolutionNode.INPUT_TYPES()
    assert "required" in inputs
    assert "tradition" in inputs["required"]
    assert inputs["required"]["tradition"][1]["default"] == "chinese_xieyi"


def test_evolution_node_return_types():
    from nodes import VULCAEvolutionNode
    assert VULCAEvolutionNode.RETURN_TYPES == ("STRING",)
    assert VULCAEvolutionNode.RETURN_NAMES == ("evolution_json",)
    assert VULCAEvolutionNode.CATEGORY == "VULCA"


def test_traditions_node_input_types():
    from nodes import VULCATraditionsNode
    inputs = VULCATraditionsNode.INPUT_TYPES()
    # No required inputs
    assert inputs.get("required", {}) == {}


def test_traditions_node_return_types():
    from nodes import VULCATraditionsNode
    assert VULCATraditionsNode.RETURN_TYPES == ("STRING",)
    assert VULCATraditionsNode.RETURN_NAMES == ("traditions_json",)
    assert VULCATraditionsNode.CATEGORY == "VULCA"


def test_layers_export_node_input_types():
    from nodes import VULCALayersExportNode
    inputs = VULCALayersExportNode.INPUT_TYPES()
    assert "required" in inputs
    assert "artwork_dir" in inputs["required"]
    assert "format" in inputs["required"]
    assert inputs["required"]["format"][1]["default"] == "png"


def test_layers_export_node_return_types():
    from nodes import VULCALayersExportNode
    assert VULCALayersExportNode.RETURN_TYPES == ("STRING",)
    assert VULCALayersExportNode.RETURN_NAMES == ("export_path",)
    assert VULCALayersExportNode.CATEGORY == "VULCA"

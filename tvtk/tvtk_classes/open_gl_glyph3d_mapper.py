# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.glyph3d_mapper import Glyph3DMapper


class OpenGLGlyph3DMapper(Glyph3DMapper):
    """
    OpenGLGlyph3DMapper - OpenGLGlyph3D on the GPU.
    
    Superclass: Glyph3DMapper
    
    Do the same job than Glyph3D but on the GPU. For this reason, it
    is a mapper not a PolyDataAlgorithm. Also, some methods of
    OpenGLGlyph3D don't make sense in OpenGLGlyph3DMapper:
    generate_point_ids, old-style set_source, point_ids_name, is_point_visible.
    
    Implementation:
    
    See Also:
    
    OpenGLGlyph3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLGlyph3DMapper, obj, update, **traits)
    
    _updateable_traits_ = \
    (('immediate_mode_rendering', 'GetImmediateModeRendering'),
    ('scale_factor', 'GetScaleFactor'), ('source_indexing',
    'GetSourceIndexing'), ('orientation_mode', 'GetOrientationMode'),
    ('selection_color_id', 'GetSelectionColorId'),
    ('scalar_material_mode', 'GetScalarMaterialMode'), ('scaling',
    'GetScaling'), ('nested_display_lists', 'GetNestedDisplayLists'),
    ('color_mode', 'GetColorMode'), ('static', 'GetStatic'),
    ('force_compile_only', 'GetForceCompileOnly'),
    ('resolve_coincident_topology_z_shift',
    'GetResolveCoincidentTopologyZShift'), ('scalar_visibility',
    'GetScalarVisibility'), ('orient', 'GetOrient'), ('clamping',
    'GetClamping'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('interpolate_scalars_before_mapping',
    'GetInterpolateScalarsBeforeMapping'), ('debug', 'GetDebug'),
    ('scale_mode', 'GetScaleMode'), ('progress_text', 'GetProgressText'),
    ('use_lookup_table_scalar_range', 'GetUseLookupTableScalarRange'),
    ('range', 'GetRange'), ('abort_execute', 'GetAbortExecute'),
    ('scalar_mode', 'GetScalarMode'), ('resolve_coincident_topology',
    'GetResolveCoincidentTopology'), ('release_data_flag',
    'GetReleaseDataFlag'), ('masking', 'GetMasking'), ('reference_count',
    'GetReferenceCount'), ('progress', 'GetProgress'),
    ('resolve_coincident_topology_polygon_offset_faces',
    'GetResolveCoincidentTopologyPolygonOffsetFaces'),
    ('global_immediate_mode_rendering',
    'GetGlobalImmediateModeRendering'), ('scalar_range',
    'GetScalarRange'), ('render_time', 'GetRenderTime'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clamping', 'debug',
    'global_immediate_mode_rendering', 'global_warning_display',
    'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
    'masking', 'nested_display_lists', 'orient', 'release_data_flag',
    'scalar_visibility', 'scaling', 'source_indexing', 'static',
    'use_lookup_table_scalar_range', 'color_mode', 'orientation_mode',
    'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode',
    'scale_mode', 'force_compile_only', 'progress_text', 'range',
    'render_time', 'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range', 'scale_factor',
    'selection_color_id'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLGlyph3DMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLGlyph3DMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clamping', 'global_immediate_mode_rendering',
            'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
            'masking', 'nested_display_lists', 'orient', 'scalar_visibility',
            'scaling', 'source_indexing', 'static',
            'use_lookup_table_scalar_range'], ['color_mode', 'orientation_mode',
            'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode',
            'scale_mode'], ['force_compile_only', 'range', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range', 'scale_factor',
            'selection_color_id']),
            title='Edit OpenGLGlyph3DMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLGlyph3DMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


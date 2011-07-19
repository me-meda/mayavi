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

from tvtk.tvtk_classes.poly_data_writer import PolyDataWriter


class CGMWriter(PolyDataWriter):
    """
    CGMWriter - write polygonal data as a CGM file
    
    Superclass: PolyDataWriter
    
    CGMWriter writes CGM (Computer Graphics Metafile) output. CGM is a
    2d graphics vector format typically used by large plotters. This
    writer can handle vertices, lines, polygons, and triangle strips in
    any combination. Colors are specified either 1) from cell scalars
    (assumed to be RGB or RGBA color specification), 2) from a specified
    color; or 3) randomly assigned colors.
    
    Note: During output of the polygonal data, triangle strips are
    converted to triangles, and polylines to lines. Also, due to
    limitations in the CGM color model, only 256 colors are available to
    the color palette.
    
    Caveats:
    
    The class ImageToPolyDataFilter is convenient for converting a
    raster image into polygons (and color map) suitable for plotting with
    CGM.
    
    See Also:
    
    PolyDataWriter PointDataToCellData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCGMWriter, obj, update, **traits)
    
    color_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'random_colors': 2, 'specified_color': 1}), help=\
        """
        Control how output polydata is colored. By default
        (_color_mode_to_default), if per cell colors are defined (unsigned
        chars of 1-4 components), then the cells are colored with these
        values. (If point colors are defined and cell colors are not, you
        can use PointDataToCellData to convert the point colors to
        cell colors.) Otherwise, by default, the cells are set to the
        specified color. If color_mode_to_specified_color is set, then the
        primitives will all be set to this color. If
        color_mode_to_random_colors is set, each cell will be randomly
        assigned a color.
        """
    )
    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    sort = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Turn on/off the sorting of the cells via depth. If enabled,
        polygonal cells will be sorted from back to front, i.e., a
        Painter's algorithm sort.
        """
    )
    def _sort_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSort,
                        self.sort)

    specified_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )
    def _specified_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpecifiedColor,
                        self.specified_color, False)

    resolution = traits.Trait(10000, traits.Range(100, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the resolution of the CGM file. This number is used to
        integerize the maximum coordinate range of the plot file.
        """
    )
    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    def _get_viewport(self):
        return wrap_vtk(self._vtk_obj.GetViewport())
    def _set_viewport(self, arg):
        old_val = self._get_viewport()
        self._wrap_call(self._vtk_obj.SetViewport,
                        deref_vtk(arg))
        self.trait_property_changed('viewport', old_val, arg)
    viewport = traits.Property(_get_viewport, _set_viewport, help=\
        """
        Specify a Viewport object to be used to transform the
        PolyData points into 2d coordinates. By default (no
        Viewport specified), the point coordinates are generated by
        ignoring the z values. If a viewport is defined, then the points
        are transformed into viewport coordinates.
        """
    )

    _updateable_traits_ = \
    (('sort', 'GetSort'), ('vectors_name', 'GetVectorsName'),
    ('tensors_name', 'GetTensorsName'), ('specified_color',
    'GetSpecifiedColor'), ('file_type', 'GetFileType'), ('file_name',
    'GetFileName'), ('scalars_name', 'GetScalarsName'), ('header',
    'GetHeader'), ('color_mode', 'GetColorMode'), ('normals_name',
    'GetNormalsName'), ('t_coords_name', 'GetTCoordsName'),
    ('field_data_name', 'GetFieldDataName'), ('pedigree_ids_name',
    'GetPedigreeIdsName'), ('global_ids_name', 'GetGlobalIdsName'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('lookup_table_name', 'GetLookupTableName'),
    ('write_to_output_string', 'GetWriteToOutputString'), ('debug',
    'GetDebug'), ('progress_text', 'GetProgressText'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('reference_count', 'GetReferenceCount'), ('progress', 'GetProgress'),
    ('resolution', 'GetResolution'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'color_mode',
    'file_type', 'field_data_name', 'file_name', 'global_ids_name',
    'header', 'lookup_table_name', 'normals_name', 'pedigree_ids_name',
    'progress_text', 'resolution', 'scalars_name', 'sort',
    'specified_color', 't_coords_name', 'tensors_name', 'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CGMWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit CGMWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['write_to_output_string'], ['color_mode',
            'file_type'], ['field_data_name', 'file_name', 'global_ids_name',
            'header', 'lookup_table_name', 'normals_name', 'pedigree_ids_name',
            'resolution', 'scalars_name', 'sort', 'specified_color',
            't_coords_name', 'tensors_name', 'vectors_name']),
            title='Edit CGMWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CGMWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

